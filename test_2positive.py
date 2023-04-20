from checkout import checkout, path_dir, path_arch


def test_step1():
    # test 1
    assert checkout('cd {}; 7z a {}'.format(path_dir, path_arch), "Everything is OK"), "Test1 Fail"


# def test_step2():
#     assert checkout('echo:"Hello"', "Hello")
#
def test_step3():
    #     # test 1
    assert checkout('cd {}; 7z u {}'.format(path_dir, path_arch), "Everything is OK"), "Test1 Fail"


def test_step4():
    #     # test 1
    assert checkout('cd {}; 7z d {}'.format(path_dir, path_arch), "Everything is OK"), "Test1 Fail"
