# mime_type_resolver.py

def resolve_mime(filename_state):
    # 1. Sanitize and extract extension state
    clean_name = filename_state.strip().lower()
    
    # 2. Mapping Directory (Extension -> MIME Type)
    mime_map = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    
    # 3. Dynamic Lookup Loop
    for ext, mime_type in mime_map.items():
        if clean_name.endswith(ext):
            return mime_type
            
    # 4. Default Fallback State
    return "application/octet-stream"

def main():
    filename = input("Enter filename: ")
    media_type = resolve_mime(filename)
    print(media_type)

main()
