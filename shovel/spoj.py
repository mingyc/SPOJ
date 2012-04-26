# -*- coding: utf-8 -*-
from sys import stderr
import urllib2
import re
import os

from shovel import task
from bs4 import BeautifulSoup
from html2text import html2text



@task
def fetch(code):
    """Fetch problem information from SPOJ.

    Download problem description from SPOJ and then create a directory that 
    contains a problem description, a sample input file and an empty python 
    template automatically.

    Args:
        code - specify the SPOJ problem to be downloaded
    """
    if not code:
        print >> stderr, __doc__
        return

    print '==== Prepare to fetch problem #{0} '.format(code)
    if len(filter(lambda l: l>0, (d.find(code) for d in os.listdir('.')))):
        print '==== Problem #{0} already downloaded!'.format(code)
        print 'Done!'
        return 
    try:
        problem_url = 'http://www.spoj.pl/problems/{0}'.format(code)
        print '==== Now downloading from {0} ...'.format(problem_url)
        problem_page = urllib2.urlopen(problem_url).read()

        print '==== Now parsing ...'
        soup = BeautifulSoup(problem_page)
        problem = soup.find('div', 'prob')
        # remove useless scripts
        while problem.script:
            problem.script.decompose()
        # remove user comments
        problem.find('div', id='ccontent').decompose()
        # remove useless divs
        while problem.div:
            problem.div.decompose()
        # remove author information
        problem.find('table', align='left').decompose()
        # remove problem type
        problem.find('h2', text=re.compile('SPOJ')).decompose()

        # retrieve problem number
        problem_num = '{0:05}'.format(int(problem.h1.string.split('.')[0]))
        # format the title
        problem.h1.string.replace_with(problem.h1.string.replace('.', '\.'))

        
        print '==== Now transforming to markdown syntax ...'
        problem_md = html2text(repr(problem).decode('utf-8', 'ignore')).encode('utf-8', 'ignore')
        # retrieve sample input data
        #input_data = 

        problem_md_dir = '{0}_{1}'.format(problem_num, code)
        print '==== Creating the directory {0}/ ...'.format(problem_md_dir)
        os.mkdir(problem_md_dir)

        problem_md_path = './{0}/{1}'.format(problem_md_dir, 'README.md')
        print '==== Writing problem details to {0} ...'.format(problem_md_path)
        with open(problem_md_path, 'w') as f:
            f.write(problem_md)

        problem_input_path = './{0}/{1}'.format(problem_md_dir, 'input')
        print '==== Attaching sample input file {0} ...'.format(problem_input_path)
        with open(problem_input_path, 'w') as f:
            f.write('\n')

        template_path = './{0}/{1}.py'.format(problem_md_dir, code)
        print '==== Attaching template file {0}...'.format(template_path)
        with open(template_path, 'w') as f:
            f.write('\n')

        print 'Done.'
    except urllib2.URLError:
        print >> stderr, '[Error] No such problem: {0}'.format(code)

    return
