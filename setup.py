from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='M Sri Sujan',
    author_email='srisujanbannu@gmail.com',
    install_requires=["langchain-huggingface","langchain","streamlit","python-dotenv","PyPDF2", "langchain_google_genai", "langchain_community", "huggingface_hub"],
    packages=find_packages()
)