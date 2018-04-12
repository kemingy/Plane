from plane import segment

def test_segment():
    text = '朋友，打 NBA2K 吗？我刚买了PS4pro，而且我有猫。'
    expect = ['朋', '友', '，', '打', ' ', 'NBA2K', ' ', '吗', '？',
              '我', '刚', '买', '了', 'PS4pro', '，', '而', '且',
              '我', '有', '猫', '。']
    assert segment(text) == expect