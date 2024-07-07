import os

def display_tree(path, indent=0):
    tree_str = ""
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        tree_str += f'{indent}{os.path.basename(root)}/\n'
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            tree_str += f'{subindent}{f}\n'
    return tree_str

# Main Method
if __name__ == '__main__':
    tree_str = display_tree("/Users/islam/chef.in")
    with open("directory_tree.txt", "w") as file:
        file.write(tree_str)
