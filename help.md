### проверка версии `pytest`
```shell
pytest --version
```

### сборка всех тестовых файлов (модулей)
```shell
pytest --collect-only
```

### Простой запуск тестов
```shell
pytest
```
_по умолчанию `pytest` будет запускать файлы только с словом `test` вначале или в конце так же и с функциями теста и классами_

### Указание пути к директории или файлу с тестами 
```shell
pytest ./
```
```shell
pytest test_functions.py
```

```shell
pytest test_functions.py
```

### запуск определенных тестов 
```shell
pytest test_functions.py -k [название подстроки]
```

### запуск определенных тестов 
```shell
pytest .\f2_class_test.py::TestClass
```
### запуск определенных тестов 
```shell
pytest .\f2_class_test.py::TestClass::test_cube
```



## Пропуск тестов
один из способов пропустить тест, это использовать `@pytest.mark.skip`

можно пропускать тесты `pytest.skip()`


для того чтоб задокументировать, по какой причине мы пропускаем тест можно написать так:
`@pytest.mark.skip(reason="Look! We are skipping this test!")`

чтоб увидеть это сообщение нужно запустить с помощью флага -rs
флаг s говорит pytest то что нужно вывести информацию о пропущенных тестах

условный пропуск тестов
`@pytest.mark.skipif()`

пропуск тестов если нет модуля
`my_import = pytest.importorskip("my_module")`




### тесты которые не проходят но их все равно нужно запустить

`@pytest.mark.xfail`

`@pytest.mark.xfail(reason="There is a bug in our implementation!")`
чтоб увидеть это сообщение нужно запустить с помощью флага -rx

условный
`@pytest.mark.xfail(
    sys.version_info > (3, 6), reason="Test requires Python version <= 3.6!"
)`


указываем, по какой причине тест должен провалиться
`@pytest.mark.xfail(raises=AssertionError)`
`@pytest.mark.xfail(raises=(AssertionError, ZeroDivisionError))`

строгий режим 
`@pytest.mark.xfail(strict=True)`

`@pytest.mark.xfail(run=False)`

## Параметризованные тесты
`@pytest.mark.parametrize("num", [1, 2, 3, 4, 5])`
`@pytest.mark.parametrize("num,ref", [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])`

`@pytest.mark.parametrize("base", [1, 2, 3])
@pytest.mark.parametrize("exponent", [4, 5, 6])`



для того чтоб можно было пропускать есть 
`@pytest.mark.parametrize("num", [1, 2, pytest.param(3, marks=pytest.mark.skip), 4, 5])`
из этого видно что `pytest.param(<значение>, marks=<метка>)`


`# Our test parametrized test
@pytest.mark.parametrize(
    "num",
    [
        pytest.param(-1, id="negative"),
        pytest.param(0, id="zero"),
        pytest.param(1, id="positive"),
    ],
)`


### FLAGS
`-vrsx`
`-collectonly`
`pytest --collectonly .\l3_skip.py`
`-k`

888888888888888888888888888888888888888
# Запуск отдельных файлов, функций, классов
# pytest 0_pytest_intro/
# pytest 0_pytest_intro/test_pytest_intro_1.py
# pytest 0_pytest_intro/test_pytest_intro_1.py::TestClass
# pytest 0_pytest_intro/test_pytest_intro_1.py::test_one

 


- Флаг управления подробностью вывода ```-v``` или ```-q```
```shell
pytest 0_pytest_intro/ -v
```

- Флаг  ```-s``` позволяет выводить принты

## Fixture
01:18
 
