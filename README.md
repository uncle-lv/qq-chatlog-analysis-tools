# qq-chatlog-analysis-tools

![license](https://img.shields.io/github/license/uncle-lv/qq-chatlog-analysis-tools) ![stars](https://img.shields.io/github/stars/uncle-lv/qq-chatlog-analysis-tools) ![issues](https://img.shields.io/github/issues/uncle-lv/qq-chatlog-analysis-tools) ![forks](https://img.shields.io/github/forks/uncle-lv/qq-chatlog-analysis-tools) ![python version](https://img.shields.io/badge/python-3.7.0-%233772A2)

a toolkit which is used for analysing QQ chatlog.

## Usage

### step1

Git clone or download source code.

```bash
git clone https://github.com/uncle-lv/qq-chatlog-analysis-tools.git
```



### step2

Setup environment.

```bash
# install virtualenv
pip install virtualenv
```

```bash
# create a virtual environment
virtualenv env
```

```bash
# activate env, use 'env\Scripts\activate' on Windows
source env/bin/activate
```

```bash
# install dependencies
pip install -r requirements.txt
```



### step3

Put your QQ chatlog into floder *in*.

<div align=center><img src="https://cdn.jsdelivr.net/gh/uncle-lv/PicX-image-hosting@main/qq-chatlog-analysis-tools/floder_in.png" alt="floder in" style="width: 200px"/></div>

### step4

Run *main.py* with chatlog‘s *filename*.

```bash
python main.py <filename.txt>
```



### step5

Now, you can check the wordcloud picture in floder *out*.

<div align=center><img src="https://cdn.jsdelivr.net/gh/uncle-lv/PicX-image-hosting@main/qq-chatlog-analysis-tools/floder_out.png" alt="floder in" style="width: 200px"/></div>

## Contributions

Any contribution you make are greatly appreciated.



## License

[MIT](https://github.com/uncle-lv/qq-chatlog-analysis-tools/blob/main/LICENSE)