class Solution:
    def simplifyPath(self, path: str) -> str:
        
        folder_stack = []

        i = 0
        current = ""
        while i < len(path) and path[i]=='/':
            i+=1
        while i < len(path):
            print(path[i], i, current, folder_stack)
            char = path[i]
            if char not in {".", "/"}:
                current += char
                i+=1
                continue
            
            if char == "/":
                if current:
                    folder_stack.append(current)
                    current = ""
                while i < len(path) and path[i] == "/":
                    i+=1
                continue

            dotString = ""
            while i < len(path) and path[i] == ".":
                dotString+=char
                i+=1

            if (i < len(path) and path[i] != "/") or current:
                current += dotString
                continue
            
            dotCount = len(dotString)
            if dotCount > 2:
                current += dotString
                continue
            
            if dotCount == 2 and folder_stack:
                folder_stack.pop()

        if current:
            folder_stack.append(current)
        
        return f"/{'/'.join(folder_stack)}"


