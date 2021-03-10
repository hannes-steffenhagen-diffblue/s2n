#!/usr/bin/env python3
import subprocess
import os
import sys

def run_make(makefile_dir, target):
    with open(os.path.join(makefile_dir, f'{target}.txt'), 'w') as out_file:
        completion = subprocess.run(
                ['make', '-C', makefile_dir, target],
                stdout=out_file,
                stderr=out_file)
    return completion.returncode



def run_test(test_dir):
    sys.stdout.write(f'Running {test_dir}: ')
    sys.stdout.flush()
    test_dir_abs = os.path.abspath(test_dir)
    run_make(test_dir_abs, 'veryclean')
    return_code = run_make(test_dir_abs, 'result')
    if return_code == 0:
        print('[SUCCESS]')
    else:
        print('[FAILURE]')


def run_all_tests():
    for filename in os.listdir('.'):
        if os.path.isdir(filename) and os.path.exists(os.path.join(filename, 'Makefile')):
            run_test(filename)


run_all_tests()
