from piece_of_cake import piece_of_cake


tests_cake = {
    'abcabcabcabc',
    'abcabcabcabc',
    'abccbaabccba',
    'ababab',
    'avav',
    'abc'
}

for idx, test_cake in enumerate(tests_cake):
    print(f'test{idx}: {test_cake} => {piece_of_cake(test_cake)}')