from plane import segment


def test_segment():
    text = '朋友，打 NBA2K 吗？我刚买了PS4pro，而且我有猫。'
    expect = ['朋', '友', '，', '打', 'NBA2K', '吗', '？',
              '我', '刚', '买', '了', 'PS4pro', '，', '而', '且',
              '我', '有', '猫', '。']
    assert segment(text) == expect

    text = 'zzz<SOS>遍身罗绮者，不是养蚕人。<EOF>zzz'
    expect = ['zzz', '<SOS>', '遍', '身', '罗', '绮', '者', '，',
              '不', '是', '养', '蚕', '人', '。', '<EOF>', 'zzz']
    assert segment(text) == expect

    text = 'pi=3.1415926，大概5%的人能接着背。'
    expect = ['pi', '=', '3.1415926', '，', '大', '概', '5%', '的',
              '人', '能', '接', '着', '背', '。']
    assert segment(text) == expect

    text = "Model #070 can't reach state-of-the-art."
    expect = ['Model', '#070', "can't", 'reach', 'state-of-the-art', '.']
    assert segment(text) == expect
