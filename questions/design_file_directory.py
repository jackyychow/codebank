# Question: Design a file-directory tree with path creation and subtree-size queries.
#

class DirNode:
    def __init__(self):
        self.children = {}   # dirname -> DirNode
        self.files = {}      # filename -> size
        self.total_size = 0  # sum of all files in subtree

class FileSystem:
    def __init__(self):
        self.root = DirNode()

    def _traverse(self, path, create=False):
        """
        Traverse to the directory node for `path`.
        path like "/a/b". Return the DirNode.
        If create=True, create dirs if missing.
        """
        # special case root
        if path == "/":
            return self.root

        parts = [p for p in path.split("/") if p]  # split and skip ""
        curr = self.root
        for p in parts:
            if p not in curr.children:
                if create:
                    curr.children[p] = DirNode()
                else:
                    raise KeyError(f"Directory {p} doesn't exist in path {path}")
            curr = curr.children[p]
        return curr

    def addDirectory(self, path):
        self._traverse(path, create=True)

    def addFile(self, path, size):
        """
        path is full file path e.g. "/a/b/file1.txt"
        We need to update all ancestor total_size with delta.
        """
        parts = [p for p in path.split("/") if p]
        if not parts:
            raise ValueError("file path invalid")

        dir_parts, file_name = parts[:-1], parts[-1]

        # walk/create dirs
        curr = self.root
        nodes_on_path = [curr]  # we keep ancestors for size propagation
        for d in dir_parts:
            if d not in curr.children:
                curr.children[d] = DirNode()
            curr = curr.children[d]
            nodes_on_path.append(curr)

        # old size?
        old_size = curr.files.get(file_name, 0)
        delta = size - old_size

        # update file size
        curr.files[file_name] = size

        # propagate delta up the chain
        for node in nodes_on_path:
            node.total_size += delta

    def getSize(self, path):
        node = self._traverse(path, create=False)
        return node.total_size