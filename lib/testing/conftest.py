def pytest_itemcollected(item):
    # Extract parent and node objects
    parent_obj = getattr(item.parent, 'obj', None)
    node_obj = getattr(item, 'obj', None)

    # Extract prefix and suffix from parent and node docstrings or names
    prefix = getattr(parent_obj, '__doc__', '').strip() if parent_obj else ''
    suffix = getattr(node_obj, '__doc__', '').strip() if node_obj else ''

    if not suffix:
        suffix = getattr(node_obj, '__name__', '')

    if not prefix:
        prefix = getattr(parent_obj, '__class__', {}).get('__name__', '')

    # Concatenate prefix and suffix to form the new nodeid
    new_nodeid = ' '.join(filter(None, (prefix, suffix)))

    # Update the item nodeid
    if new_nodeid:
        item._nodeid = new_nodeid
