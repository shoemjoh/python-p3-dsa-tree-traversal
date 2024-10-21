class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    node = self.root
    nodes_to_visit = [node]

    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop(0)

      if current_node['id'] == id:
        return current_node
      else:
        nodes_to_visit = current_node['children'] + nodes_to_visit

    return None

