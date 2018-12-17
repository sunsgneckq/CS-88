test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> raquels_car = Car('Tesla')
          >>> raquels_car.model
          'Tesla'
          >>> raquels_car.gas = 10
          >>> raquels_car.drive()
          'Tesla goes vroom!'
          >>> raquels_car.drive()
          'Tesla cannot drive!'
          >>> raquels_car.fill_gas()
          Your car is full.
          >>> raquels_car.gas
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> raquels_car = Car('Tesla')
          >>> Car.headlights
          2
          >>> raquels_car.headlights
          2
          >>> Car.headlights = 3
          >>> raquels_car.headlights
          3
          >>> raquels_car.headlights = 2
          >>> Car.headlights
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> raquels_car = Car('Tesla')
          >>> raquels_car.wheels = 2
          >>> raquels_car.wheels
          2
          >>> Car.num_wheels
          4
          >>> raquels_car.drive()
          'Tesla cannot drive!'
          >>> Car.drive()
          Error
          >>> Car.drive(raquels_car)
          'Tesla cannot drive!'
          >>> MonsterTruck.drive(raquels_car)
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> sumukhs_car = MonsterTruck('Batmobile')
          >>> sumukhs_car.drive()
          238e48b17a8085331a1d671045b7a572
          3a03e21a02df84fa20699bc73c3c942b
          # locked
          >>> Car.drive(sumukhs_car)
          3a03e21a02df84fa20699bc73c3c942b
          # locked
          >>> MonsterTruck.drive(sumukhs_car)
          238e48b17a8085331a1d671045b7a572
          3a03e21a02df84fa20699bc73c3c942b
          # locked
          >>> Car.rev(sumukhs_car)
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
