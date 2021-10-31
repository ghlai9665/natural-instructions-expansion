from test_utils import rename_categories

# test rename_category
def test_rename_categories():
    data = {"Categories": ["old1", "old2", "old3"]}
    new_data = rename_categories({"old1": "new1", "old2": "new2"}, data)
    assert new_data == {'Categories': ['new1', 'new2', 'old3']}