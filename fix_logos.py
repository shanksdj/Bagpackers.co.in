import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # We want to replace any <img ...> that is directly preceded by <a ...> inside <div class="logo"> or <div class="nav-logo"> or similar.
    # Actually, simpler: just find any <img ...> that has src ending in a logo variant and replace it.
    
    # Or replace any <img ...> inside a logo div.
    # Regex to find <div class="[^"]*logo[^"]*"> ... <img ...>
    
    # Let's cleanly replace things that look like logos.
    # We remove srcset and set src to images/goa-tour/image.png
    
    new_content = re.sub(
        r'<img\s+[^>]*src="([^"]*(logo2|2|lo|logoimage|logo2-700|scuba15-700)\.(webp|png))"[^>]*>',
        '<img src="images/goa-tour/image.png" alt="goa tour packages" title="goa tour packages">',
        content,
        flags=re.IGNORECASE
    )
    
    with open(file, 'w') as f:
        f.write(new_content)

print("Done")
