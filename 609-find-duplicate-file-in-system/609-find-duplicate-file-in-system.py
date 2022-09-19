class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for i in paths:
            root_directory, *files = i.split(" ")
            
            for file in files:
                file_name, content = file.split("(")
                d[content[:-1]].append(root_directory + "/" + file_name)
                
        return [i for k, i in d.items() if len(i) > 1]
    