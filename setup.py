from setuptools import setup, find_packages

setup(
    name='minigrid_hci',
    version='0.0',
    description='Package for training agents from demonstration using MiniGrid, forked from project by francidellungo.',
    author='Sam Powers',
    author_email='snpowers@cs.cmu.edu',
    packages=find_packages(),
    install_requires=['setuptools==59.5.0',
                      'minigrid',
                      'gym<=0.25.2',
                      'gym_minigrid',
                      'argcomplete',
                      'termcolor',
                      'modelsummary',
                      'tensorboardx',
                      'scikit-learn',
                      'tensorboard',
                      'numpy==1.23.5'
                    ]
)
