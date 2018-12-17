test = {
  'name': 'call-expressions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from operator import mul, add
          >>> mul(3, 4)
          12
          >>> mul(3, add(4, 1))
          15
          >>> pow(2, 3)
          8
          >>> pow(pow(2, 3), abs(-2))
          64
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from math import sqrt
          >>> sqrt(144)
          12
          >>> pi
          Error
          >>> from math import pi
          >>> pi # round to 2 decimal places
          3.14
          >>> from operator import add
          >>> print(add(9, 1))
          10
          >>> print(print(2))
          2
          None
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
