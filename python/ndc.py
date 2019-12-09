from typing import Optional


def ndc_format(s: Optional[str]) -> Optional[str]:
    if not s:
        return
    labeler, product, package = s.split('-')
    return '-'.join((labeler.zfill(5), product.zfill(4), package.zfill(2)))


if __name__ == '__main__':
    ex1 = '0002-0610-01'  # 00002-0610-01
    ex2 = '55513-710-01'  # 55513-0710-01
    ex3 = '33311-0780-1'  # 33311-0780-01

    for code in (ex1, ex2, ex3):
        print(ndc_format(code))

