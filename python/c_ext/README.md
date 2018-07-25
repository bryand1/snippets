# Python modules in C

```bash
python setup.py build_ext --inplace
```

```python
import _chi2
print(_chi2.chi2(2.0, 1.0, [-1.0, 4.2, 30.6], [-1.5, 8.0, 63.0], [1.0, 1.5, 0.6])))
# 2.89888888889
```

[Python modules in C](https://dfm.io/posts/python-c-extensions/)

