from checkout import checkout, path_dir, path_arch

path_to_dir = '/home/user/out'


def test_step5():
    # test 1
    assert checkout('cd {}; 7z e {} -o{} -y'.format(path_dir, path_arch, path_to_dir),
                    "Is not archive"), "Test1 Fail"

# def test_step6():
#     #     # test 1
#     assert checkout('cd {}; 7z t {}'.format(path_dir, path_arch), "Everything is OK"), "Test1 Fail"
