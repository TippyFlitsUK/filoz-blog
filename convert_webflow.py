#!/usr/bin/env python3
"""
Convert Webflow template to Hugo index.html
Keeps everything the same except replaces event cards with Hugo blog loop
"""

import re

# Read the Webflow HTML
with open('filoz-template/Events _ FilOz.html', 'r') as f:
    html = f.read()

# Fix asset paths throughout
html = html.replace('./Events _ FilOz_files/', '/')
html = html.replace('href="https://www.filoz.org/events"', 'href="/"')
html = html.replace('href="https://medium.com/@filoz"', 'href="/"')

# Hugo template for a single blog post card (based on event card structure)
hugo_blog_card = '''{{ range .Site.RegularPages }}
                <a href="{{ .Permalink }}" class="event_featured-item intern w-inline-block">
                    <div class="event-image">
                        {{ if .Params.cover.image }}
                        <img src="{{ .Params.cover.image }}" loading="lazy" alt="{{ .Title }}">
                        {{ else }}
                        <img src="/images/filoz-avatar.png" loading="lazy" alt="{{ .Title }}">
                        {{ end }}
                    </div>
                    <div class="event_featured-item-content intern">
                        <div class="margin-bottom margin-small">
                            <h2 class="text-size-large light-blue">{{ .Title }}</h2>
                        </div>
                        <p class="text-size-regular gray-soft">{{ if .Description }}{{ .Description }}{{ else }}{{ .Summary | truncate 200 }}{{ end }}</p>
                        <div class="margin-top margin-xmedium">
                            <div class="event_multi-image-item">
                                <div class="text-size-small black">By:</div>
                                <img loading="lazy" src="/images/filoz-avatar.png" alt="FilOz" class="event_avatar">
                                <div class="w-layout-hflex company-name-wrap">
                                    <div class="text-size-small gray">{{ if .Params.author }}{{ .Params.author }}{{ else }}FilOz{{ end }}</div>
                                </div>
                            </div>
                        </div>
                        <div class="margin-top margin-small">
                            <div class="event_tag-wrapper">
                                <div class="w-layout-vflex tags-wrapper">
                                    <div class="tag">
                                        <div class="event-header6_icon-wrapper">
                                            <div class="icon-embed-xsmall w-embed">
                                                <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                    <g clip-path="url(#clip0)">
                                                        <path d="M6 3V6L8 7M11 6C11 8.76142 8.76142 11 6 11C3.23858 11 1 8.76142 1 6C1 3.23858 3.23858 1 6 1C8.76142 1 11 3.23858 11 6Z" stroke="#0090FF" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                                    </g>
                                                    <defs>
                                                        <clippath id="clip0">
                                                            <rect width="12" height="12" fill="white"/>
                                                        </clippath>
                                                    </defs>
                                                </svg>
                                            </div>
                                        </div>
                                        <div class="text-size-small">{{ .Date.Format "Jan 2, 2006" }}</div>
                                    </div>
                                </div>
                                <div class="button-group-3">
                                    <div class="arrow-button pad">
                                        <div class="title-wrapper">
                                            <p class="button-title">Read More</p>
                                            <div class="arrow-wrapper">
                                                <img src="/images/icons/arrow-up-right.svg" loading="lazy" alt="" class="button-arrow">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </a>
                {{ end }}'''

# Find and replace the event cards section
# The collection list contains all the event cards
collection_start = html.find('<div role="list" class="collection-list w-dyn-items">')
collection_end = html.find('</div></div></div></div></section>', collection_start)

if collection_start > 0 and collection_end > 0:
    # Replace just the content inside collection-list
    before = html[:collection_start + len('<div role="list" class="collection-list w-dyn-items">')]
    after = html[collection_end:]

    # Write the final Hugo template
    output = before + '\n' + hugo_blog_card + '\n' + after

    # Change title from "Events | FilOz" to use Hugo variable
    output = output.replace('<title>Events | FilOz</title>', '<title>{{ .Site.Title }}</title>')

    # Save to layouts/index.html
    with open('layouts/index.html', 'w') as f:
        f.write('{{ define "main" }}\n')
        # Write everything from <div class="page-wrapper"> onwards
        page_wrapper_start = output.find('<div class="page-wrapper">')
        page_wrapper_end = output.rfind('</body>')
        f.write(output[page_wrapper_start:page_wrapper_end])
        f.write('\n{{ end }}\n')

    print("✓ Created layouts/index.html")
    print(f"✓ Replaced event cards with Hugo blog loop")
    print(f"✓ Fixed all asset paths")
else:
    print("ERROR: Could not find collection list section")
