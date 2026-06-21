# Pandas #

<img src="G:\01资料\Pictures\pandas标签云.png" style="zoom:80%;" />



*<span style='color: blue;font-size: 18px'>[引言]   基本数据结构</span>*

**:a:** Series

​	**`Series`是一个一维的带标签的数组，可以保存任意数据类型（整数、字符串、浮点数、Python对象等），轴标签统称为索引。**



**:b:**DataFrame

​	**`DataFrame`是一个二维带标签的数据结构，用于保存数据，例如二维数组或者是具有行和列的列表，你可以将其想象成电子表格，SQL表或者`Series`对象的字典。**





# 一、Pandas的数据结构

## 1、Series 

### # Series简介

#### # Series类似于ndarray

​	**`Series`的作用与ndarray非常相似，并且是大多数NumPy函数的有效参数。但是，切片之类的操作仅仅只会对索引进行切片。**

​	**与NumPy数组类似，pandas的Series也有一个dtype，这通常是NumPy的数据类型，但是Pandas和第三方库扩展了NumPy的数据类型，数据类型可能是`ExtensionDtype`。**



```python
s1 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print("=============原Series==============")
print(s1)
print("=============取Series的第一个数据==============")
print(s1.iloc[0])
print("=============取Series的前三个数据==============")
print(s1.iloc[:3])
print("=============取Series的第4,2,3个数据==============")
print(s1.iloc[[3, 1, 2]])
print("=============Series的数据,自然底数e的多少次方==============")
print(np.exp(s1))
print("=============取Series中大于平均数的数据==============")
print(s1[s1 > s1.mean()])



#输出结果如下
=============原Series==============
a   -0.844990
b    0.187121
c    1.292373
d   -0.665453
e    0.056361
dtype: float64
=============取Series的第一个数据==============
-0.8449900086361438
=============取Series的前三个数据==============
a   -0.844990
b    0.187121
c    1.292373
dtype: float64
=============取Series的第4,2,3个数据==============
d   -0.665453
b    0.187121
c    1.292373
dtype: float64
=============Series的数据,自然底数e的多少次方==============
a    0.429562
b    1.205774
c    3.641416
d    0.514041
e    1.057980
dtype: float64
=============取Series中大于平均数的数据==============
b    0.187121
c    1.292373
e    0.056361
dtype: float64
```



**虽然`Series`类似于ndarray，但如果需要实际的ndarray，请使用`Series.to_numpy()`**

```python
>>> s1.to_numpy()
array([-0.84499001,  0.18712146,  1.29237261, -0.66545261,  0.05636128])
```





#### # Series类似于字典

​	**Series类似于固定大小的字典，你可以通过索引标签来获取和设置值，如果没有对应的索引标签，则会引发[KeyError][]**



```python
s1 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print("=============原Series==============")
print(s1)
print("=============获取Series中索引a对应的元素==============")
print(s1['a'])
print("=============修改Series中索引d对应的元素为10==============")
s1['d'] = 10
print(s1)
print("=============判断f在不在Series的索引中==============")
print('f' in s1)
print("=============赋值并添加f==============")
s1['f'] = 12
print(s1)
print(f"a in s1 : {'a' in s1}")
print(f"f in s1 : {'f' in s1}")
print("=============使用get方法获取Series中索引c对应的元素==============")
print(s1.get('c'))
print("=============类似字典的操作s[key] = s.get(k, value)==============")
s1['h'] = s1.get('h', 1.0)
print(s1)


#输出结果如下
=============原Series==============
a   -1.085966
b   -1.162634
c   -0.214699
d    1.340563
e    0.269808
dtype: float64
=============获取Series中索引a对应的元素==============
-1.0859659848856196
=============修改Series中索引d对应的元素为10==============
a    -1.085966
b    -1.162634
c    -0.214699
d    10.000000
e     0.269808
dtype: float64
=============判断f在不在Series的索引中==============
False
=============赋值并添加f==============
a    -1.085966
b    -1.162634
c    -0.214699
d    10.000000
e     0.269808
f    12.000000
dtype: float64
a in s1 : True
f in s1 : True
=============使用get方法获取Series中索引c对应的元素==============
-0.21469889731018935
=============类似字典的操作s[key] = s.get(k, value)==============
a    -1.085966
b    -1.162634
c    -0.214699
d    10.000000
e     0.269808
f    12.000000
h     1.000000
dtype: float64

```



#### # 向量化操作和Series的标签对齐

​	**向量化操作：NumPy数组中的元素作运算时，不需要遍历整个数组，直接在ndarray层面上作运算即可，在Pandas中也是如此。**

​	**标签对齐：Series和ndarray的一个关键区别就是Series会自动通过标签对齐数据，因此，编写代码时，你无需考虑Series所涉及的数据是否具有相同的标签，因为未对齐标签的运算结果会被标记为`NaN`。**



```python
print("================NumPy的操作===================")
data = np.random.randint(10, size=5)
print(f"原数组：{data}")
print(f"data[1:] + data[:-1] = {data[1:] + data[:-1]}")
print("================Pandas的操作===================")
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print("=============原Series==============")
print(s)
print("=============Series的元素除2取整数部分==============")
print(s // 2)
print("=============Series的元素x2==============")
print(s + s)
print("=============Series的元素的exp(s)==============")
print(np.exp(s))
print("===Series[1:]==========Series[:-1]==============")
print(s[1:], s[:-1])
print("=============Series[1:] + Series[:-1]==============")
print(s[1:] + s[:-1])


#运行结果如下
================NumPy的操作===================
原数组：[9 0 0 9 3]
data[1:] + data[:-1] = [ 9  0  9 12]
================Pandas的操作===================
=============原Series==============
a    9
b    0
c    0
d    9
e    3
dtype: int32
=============Series的元素除2取整数部分==============
a    4
b    0
c    0
d    4
e    1
dtype: int32
=============Series的元素x2==============
a    18
b     0
c     0
d    18
e     6
dtype: int32
=============Series的元素的exp(s)==============
a    8103.083928
b       1.000000
c       1.000000
d    8103.083928
e      20.085537
dtype: float64
===Series[1:]==========Series[:-1]==============
b    0						a    9
c    0						b    0
d    9						c    0
e    3						d    9
dtype: int32				dtype: int32
=============Series[1:] + Series[:-1]==============
a     NaN				#a未对齐所以是NaN
b     0.0
c     0.0
d    18.0
e     NaN				#e未对齐所以是NaN
dtype: float64
```







### （1）构造函数

**==pandas.Series(*data=None, index=None, dtype=None, name=None, copy=False*)==**

​	**带有轴标签的一维ndarray，包括时间序列。**

​	**标签不必唯一，但必须是可哈希类型。该对象支持基于整数和标签的索引，并提供大量用于执行涉及索引操作的方法。**

​	*一个对象如果具有在其生命期内绝不改变的哈希值，并可以同其他对象进行比较就被称为 **可哈希** 对象。*



| 参数： |
| ------ |

**①data：array-like，iterable, dict或标量**

​	**包含Series中存储的数据。如果数据为字典，则参数顺序保持不变。**

**②index：array-like或一维索引**

​	**其值必须是可哈希的，且长度要与`data`的长度相同。允许使用重复的索引值，如果未提供，则默认为RangeIndex(0, 1, ..., n)。如果数据为`dict`且索引为None，则使用`dict`中的键作为索引。如果索引不为None，则生成的Series将使用给定的索引值。**

**③dtype：str, numpy.dtype或ExtensionDtype， 可选**

​	**输出的`Seires`的数据类型，如果未指定，则根据data推断。**

**④name：Hashable，默认为`None`**

​	**赋予该系列的名称**

**⑤copy：bool，默认False**

​	**复制输入数据，仅影响`Series`或一维数组的输入。**



**:a:使用`copy=False`从<span style='color: #D15511'>列表</span>中构建Series，这时`Series`保存的只是原始数据的** <span style='color: blue; font-size: 19px'>***副本***</span>

```python
>>> r = [1, 2]
>>> ser = pd.Series(r, copy=False)
>>> ser.iloc[0] = 999
>>> r
[1, 2]
>>> ser
0    999
1      2
dtype: int64
```



**:b:使用`copy=False`从<span style='color: #D15511'>一维ndarray</span>中构建Series，这时`Series`保存的是原始数据的** <span style='color: red; font-size: 19px'>***视图***</span>**

```python
>>> r = np.array([1, 2])
>>> ser = pd.Series(r, copy=False)
>>> ser.iloc[0] = 999
>>> r
array([999,   2])
>>> ser
0    999
1      2
dtype: int64
```





#### # From ndarray

​	**如果`data`是ndarray，则<span style='color: red'>index的长度必须与data的长度相同。</span>如果没有指定index，则会创建一个包含`values[0, ..., len(data) - 1]`的索引**



```python
import pandas as pd
import numpy as np
s1 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s2 = pd.Series(np.random.randn(5), index=['a', 'b', 'a', 'd', 'e'])
s3 = pd.Series(np.random.randn(5))
print(s1)
print(s2)							#s2中有两个重复的索引值，这是允许的
print(s3)							#可以看到，不指定index，会自动创建0 —— len(data)-1的索引



#运行结果如下
a    1.599401
b    0.107346
c   -0.365301
d    0.113969
e   -1.179075
dtype: float64
a    0.442143
b    0.093886
a   -0.116874
d    1.291217
e   -0.661519
dtype: float64
0   -0.708995
1    0.066932
2   -0.335987
3   -1.809913
4    1.269350
dtype: float64
```



#### # From dict

​	**如果`data`是字典，索引首先会使用字典中的键构建，之后，如果给定了index，则会使用给定的index重新构建索引。若字典的某个键不在index的列表中，则该索引所对应的数据将为`NaN`**



```python
data = {'a': 1.2, 'b': 2.3, 'c': 2.0}
d1 = pd.Series(data)
d2 = pd.Series(data, index=['b', 'c', 'd', 'a'])
print(d1)
print(d2)


#运行结果如下
a    1.2
b    2.3
c    2.0
dtype: float64
b    2.3
c    2.0
d    NaN
a    1.2
dtype: float64
```



#### # From scalar value

​	**如果data是标量值，则尽可能提供索引，该值将重复以匹配索引的长度**



```python
s1 = pd.Series(5)
s2 = pd.Series(5.0, index=[2, 4, 5])
print(s1)
print(s2)

#运行结果如下
0    5
dtype: int64
2    5.0
4    5.0
5    5.0
dtype: float64
```





### （2）属性

#### Series.index

​	**返回Series的索引（轴标签）**

```python
>>> cities = ['Kolkata', 'Chicago', 'Toronto', 'Lisbon']
>>> populations = [14.85, 2.71, 2.93, 0.51]
>>> city_series = pd.Series(populations, index=cities)
>>> city_series.index
Index(['Kolkata', 'Chicago', 'Toronto', 'Lisbon'], dtype='object')
```



#### Series.dtype

​	**返回底层数据的dtype对象**

```python
s = pd.Series([1, 2, 3])
>>> s.dtype
dtype('int64')
```



#### Series.size

​	**返回基础数据中的元素数量**

```python
s = pd.Series(['Ant', 'Bear', 'Cow'])
>>> s
0     Ant
1    Bear
2     Cow
dtype: object
>>> s.size
3
```



#### Series.T

​	**返回转置，根据定义是它本身**

```python
s = pd.Series(['Ant', 'Bear', 'Cow'])
>>> s
0     Ant
1    Bear
2     Cow
dtype: object
>>> s.T
0     Ant
1    Bear
2     Cow
dtype: object
```



#### Series.name

​	**返回Series的名称，如果Series用于构成DataFrame，其名称将成为其索引或列名。**

```python
s = pd.Series([1, 2, 3], dtype=np.int64, name='Numbers')
>>> s
0    1
1    2
2    3
Name: Numbers, dtype: int64
>>> s.name = "Integers"			  		#修改名称
>>> s
0    1
1    2
2    3
Name: Integers, dtype: int64


df = pd.DataFrame([[1, 2], [3, 4], [5, 6]],
                  columns=["Odd Numbers", "Even Numbers"])
>>> df
   Odd Numbers  Even Numbers
0            1             2
1            3             4
2            5             6

>>> df["Even Numbers"].name			#Series用于构成DataFrame时，其名称可以作为索引，也可以作为列名
'Even Numbers'
```



#### Series.hasnans

​	**如果有任何NaN，则返回True**

```python
s = pd.Series([1, 2, 3, None])
>>> s
0    1.0
1    2.0
2    3.0
3    NaN
dtype: float64
>>> s.hasnans
True
```



#### Series.values

​	**返回Series中的值**



```python
>>> pd.Series([1, 2, 3]).values
array([1, 2, 3])
>>> pd.Series(list('aabc')).values
array(['a', 'a', 'b', 'c'], dtype=object)
```



#### Series.is_unique

​	**返回布尔值，如果Series中的值是唯一的，则返回`True`，否则返回`False`**



```python
s = pd.Series([1, 2, 3])
>>> s.is_unique
True
s = pd.Series([1, 2, 3, 1])
>>> s.is_unique
False
```







### （3）方法

#### Series.to_dict

**==Series.to_dict()==**

​	**将Series转成字典，其中字典的键为Series的label，值为Series的value**



#### Series.to_numpy

**==Series.to_numpy(*dtype=None*)==**

​	**将Series转成NumPy的ndarray，dtype用于指定数据类型**











## 2、DataFrame

### # DataFrame创建

​		**DataFrame是一个二维带标签的数据结构，其列可能包含不同类型的数据。你可以将其想象成Excel，SQL表，或者Series对象的字典。DataFrame接受多种不同类型的输入：**

- **一维ndarrays、列表、字典或Series**
- **二维numpy.ndarray**
- **结构化数组、记录数组（可通过属性访问）**
- **一个Series**
- **其他DataFrame**



#### # From dict

​	**对于一般的字典来说，键值对`{key: value}`的key是DataFrame的列，value是DataFrame的值，index没给出则自动生成。**

​	**对于字典嵌套字典，例如`{key1: {key2: value}}`，此时Pandas会把`key1`当成DataFrame的列，`key2`当成DataFrame的索引，`value`当成DataFrame的值来创建DataFrame对象**

:one:**一般的字典：**

```python
>>> d = {'col1': [1, 2], 'col2': [3, 4]}
>>> df = pd.DataFrame(data=d, dtype=int32)
>>> df			   #数据类型为np.int32
   col1  col2
0     1     3
1     2     4
```



**:two:包含Series的字典**

```python
d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}
df = pd.DataFrame(d)
>>> df
   one  two
a  1.0  1.0
b  2.0  2.0
c  3.0  3.0
d  NaN  4.0


>>> pd.DataFrame(d, index=["d", "b", "a"])
   one  two
d  NaN  4.0
b  2.0  2.0
a  1.0  1.0

>>> pd.DataFrame(d, index=["d", "b", "a"], columns=["two", "three"])
   two three
d  4.0   NaN
b  2.0   NaN
a  1.0   NaN
```



**:three:包含list和ndarray的字典**

```python
d = {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]}

>>> pd.DataFrame(d)
   one  two
0  1.0  4.0
1  2.0  3.0
2  3.0  2.0
3  4.0  1.0
```



**:four:字典嵌套字典**

```python
d = {'a': {'col1': [1, 2]},
    'b': {'col2': [3, 4]}}
df = pd.DataFrame(d)
>>> print(df)
           a       b
col1  [1, 2]     NaN
col2     NaN  [3, 4]
```



**:five:字典嵌套元组**

```python
pd.DataFrame(
    {
        ("a", "b"): {("A", "B"): 1, ("A", "C"): 2},
        ("a", "a"): {("A", "C"): 3, ("A", "B"): 4},
        ("a", "c"): {("A", "B"): 5, ("A", "C"): 6},
        ("b", "a"): {("A", "C"): 7, ("A", "B"): 8},
        ("b", "b"): {("A", "D"): 9, ("A", "B"): 10},
    }
)


#输出结果如下，创建的时候用到了MultiIndex
       a              b      
       b    a    c    a     b
A B  1.0  4.0  5.0  8.0  10.0
  C  2.0  3.0  6.0  7.0   NaN
  D  NaN  NaN  NaN  NaN   9.0
```



#### # From ndarray

​	**对于一般的NumPy数组来说，ndarray的每一项为DataFrame的每一行，若index和columns未指定，则使用RangeIndex。**

```python
>>> df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
	                    columns=['a', 'b', 'c'])
>>> df
   a  b  c
0  1  2  3
1  4  5  6
2  7  8  9
```



​	**对于结构化数组或记录数组来说，ndarray中的某一项对应于DataFrame的某一行，其对应的字段名（属性名）为DataFrame的列，每一列都有对应的dtype、如果未指定index，则使用RangeIndex**

```python
persontype = np.dtype({
    'names': ['name', 'age', 'chinese', 'math', 'english'],
    'formats': ['S32', 'i', 'i', 'i', 'f']})


#dtype为自定义的结构化数组
peoples = np.array([
    ("ZhangFei", 32, 75, 100, 90),
    ("GuanYu", 24, 85, 96, 88.5),
    ("ZhaoYun", 28, 85, 92, 96.5),
    ("HuangZhong", 29, 65, 85, 100)
], dtype=persontype)

person_df = pd.DataFrame(peoples)
print(person_df)

#运行结果如下
            name  age  chinese  math  english
0    b'ZhangFei'   32       75   100     90.0
1      b'GuanYu'   24       85    96     88.5
2     b'ZhaoYun'   28       85    92     96.5
3  b'HuangZhong'   29       65    85    100.0
```



​	**对于列表嵌套字典的结构来说，即`[{key1: value1}, {key2: value2}, ...]`，列表的某一项(如`{key1, value1}`)为DataFrame的某一行，其中的`key`为DataFrame的列，`value`为DataFrame的值；如果未指定index，则使用RangeIndex**

```python
data2 = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]
data2_df = pd.DataFrame(data2)
print(data2_df)
data2_df = pd.DataFrame(data2, index=["one", "two"])
print(data2_df)


#输出结果如下
   a   b     c
0  1   2   NaN
1  5  10  20.0
     a   b     c
one  1   2   NaN
two  5  10  20.0
```



#### # From Series/DataFrame

​	**Series中的index为DataFrame的索引，Series.name是DataFrame的列名，Series.values是DataFrame的值，如果Series中未指定索引和列名，则使用RangeIndex**

```python
ser = pd.Series([0, 1, 2], index=list("abc"), name="ser")
serdf = pd.DataFrame(ser)
>>> print(serdf)

   ser
a    0
b    1
c    2


#两个DataFrame共享数据
>>> df1 = pd.DataFrame([1, 2, 3], index=["a", "b", "c"], columns=["x"])
>>> df2 = pd.DataFrame(data=df1, index=["a", "c"])
>>> df2
   x
a  1
c  3
```



#### # From NamedTuple

​	**`namedtuple`列表中的第一个字段名为DataFrame的列，其余的元组只需解包赋值到DataFrame的每一行，如果其中任何一个`namedtuple`比第一个短，则在相应行中后面填充NaN，否则引发[ValueError][]**

```python
from collections import namedtuple
Point = namedtuple("Point", "x y")
point_df = pd.DataFrame([Point(0, 0), Point(0, 3), (2, 3)])
>>> print(point_df)
   x  y
0  0  0
1  0  3
2  2  3

Point3D = namedtuple("Point", "x y z")
point3D_df = pd.DataFrame([Point3D(0, 0, 1), Point3D(0, 3, 2), (2, 3)])
>>> print(point3D_df)

#输出结果如下，这里可以看到第三列的数据的数据类型为float64，因为第三列z中有一个浮点数表示的NaN
   x  y    z
0  0  0  1.0
1  0  3  2.0
2  2  3  NaN
```



#### #From dataclasses

```python
from dataclasses import make_dataclass
Point = make_dataclass("Point", [("x", int), ("y", int)])
df = pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
>>> print(df)

   x  y
0  0  0
1  0  3
2  2  3
```



### （1）构造函数

**==pandas.DataFrame(*data=None, index=None, columns=None, dtype=None, copy=None*)==**

​	**该数据结构是二维的，大小可变的数据，包含带标签的轴（行和列）。算术运算与行列标签对齐。**



| 参数： |
| ------ |

**①data：ndarray（结构化或同构），iterable，dict或DataFrame**

​	**要构建DataFrame的数据**

**②index：Index或array_like**

​	**构建DataFrame需要的索引，如果未提供，则默认使用`RangeIndex(0, 1, ... n)`**

**③columns：Index或array_like**

​	**当输入数据data中没有列标签时，默认为`RangeIndex(0, 1, ..., n)`，若有，则使用给定的列标签**

**④dtype：dtype，默认None**

​	**DataFrame的数据类型**

**⑤copy：bool 或None，默认None**

​	**是否从输入的data中复制数据**









### （2）属性

#### DataFrame.index

​	**返回DataFrame的行标签。标签可以是整数、字符串或任何其他可哈希的类型。**



```python
>>> df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Aritra'],
...                    'Age': [25, 30, 35],
...                    'Location': ['Seattle', 'New York', 'Kona']},
...                   index=([10, 20, 30]))
>>> df.index
Index([10, 20, 30], dtype='int64')
```



#### DataFrame.columns

​	**返回DataFrame的列标签**

```python
>>> df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
>>> df
     A  B
0    1  3
1    2  4
>>> df.columns
Index(['A', 'B'], dtype='object')
```



#### DataFrame.values

​	**返回NumPy的ndarray，数组中仅有DataFrame的值，数组的dtype将采用隐式向上转型。**

```python
#单一数据类型
>>> df = pd.DataFrame({'age':    [ 3,  29],
...                    'height': [94, 170],
...                    'weight': [31, 115]})
>>> df
   age  height  weight
0    3      94      31
1   29     170     115
>>> df.dtypes
age       int64
height    int64
weight    int64
dtype: object
>>> df.values
array([[  3,  94,  31],
       [ 29, 170, 115]], dtype=int64)


#多种数据类型
>>> df2 = pd.DataFrame([('parrot',   24.0, 'second'),
...                     ('lion',     80.5, 1),
...                     ('monkey', np.nan, None)],
...                   columns=('name', 'max_speed', 'rank'))
>>> df2.dtypes
name          object
max_speed    float64
rank          object
dtype: object
>>> df2.values
array([['parrot', 24.0, 'second'],
       ['lion', 80.5, 1],
       ['monkey', nan, None]], dtype=object)
```







#### **DataFrame.dtypes**

​	**返回一个包含每列数据类型的Series对象，该Series的索引是原DataFrame的列。**

```python
>>> df = pd.DataFrame({'float': [1.0],
...                    'int': [1],
...                    'datetime': [pd.Timestamp('20180310')],
...                    'string': ['foo']})
>>> df.dtypes
float              float64
int                  int64
datetime    datetime64[ns]
string              object
dtype: object
```



#### DataFrame.axes

​	**返回表示DataFrame轴的列表，列表仅包含行轴标签和列轴标签，它们按顺序返回**

```python
data = {"state":["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
		"pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
>>> frame.axes
[RangeIndex(start=0, stop=6, step=1), Index(['state', 'year', 'pop'], dtype='object')]
```











## 3、Index objects

### （1）构造函数

**==pandas.Index(*data=None, dtype=None, copy=False, name=None, tupleize_cols=True*)==**

​	**用于索引和标签对齐的<span style='color: red'>不可变</span>序列，用来存储所有Pandas对象的轴标签。**

​	**Index示例只能包含可哈希对象，Index示例不能保存`np.float16`的数据类型**



| 参数： |
| ------ |

**①data：array_like(一维)**

**②dtype：str，numpy.dtype 或 ExtensionDtype， 可选**

​	**输出Index对象的数据类型，如果未指定，则从data推断**

**③copy：bool，默认False**

​	**复制输入数据**

**④name：object**

​	**索引的名称**

**⑤tupleize_cols：bool，默认为True**

​	**如果为True，则创建MultiIndex**



```python
>>> pd.Index([1, 2, 3])
Index([1, 2, 3], dtype='int64')

>>> pd.Index(list('abc'))
Index(['a', 'b', 'c'], dtype='object')

>>> pd.Index([1, 2, 3], dtype="uint8")
Index([1, 2, 3], dtype='uint8')
```



### （2）属性





# 二、索引和选择数据

## 【前言】 索引的不同选择

**Pandas现在支持三种类型的多轴索引**

**:one:`.loc`主要基于标签，也可以与布尔数组一起使用。当索引的项未找到时，`.loc`将会引发 [KeyError][]， 允许的输入有：**

- **单个标签，例如`5`或`'a'`（请注意，`5`被解释为索引的 标签，而不是索引的位置）**
- **标签列表或数组`['a', 'b', 'c']`**
- **带标签的切片对象`'a':'f'`，它包含端点`'a'`和`'f'`**
- **布尔数组（任何`NA`值都被视为False）**
- **具有一个参数的`callable`函数（调用Series或DataFrame），该函数返回索引的有效输出**
- **行（和列）的元组，其元素是上述输入之一**





**:two:`.iloc`主要基于整数位置（从轴`0`到`length - 1`），也可以和布尔数组一起使用。如果索引项下标越界，`iloc`会引发`IndexError`，除切片索引以外。允许的输入有：**

- **一个整数，例如`5`**
- **整数列表或数组，例如`[4, 3, 0]`**

- **ints的切片对象，`1:7`**
- **布尔数组（任何`NA`都将被视为`False`）**
- **具有一个参数的`callable`函数（调用Series或DataFrame），该函数返回索引的有效输出**
- **行（和列）的元组，其元素是上述输入之一**



**:three:`.loc`, `.iloc`和`[]`可以接受一个`callable`作为索引器**



*<span style='font-size: 20px; color: red'>在Pandas3.0中，链式索引将不起作用，不要使用链式索引！！！</span>*





## 1、基础知识

**下表显示了使用`[]`索引Pandas对象时的返回值类型：**

| 对象类型  |      选择       |      返回值类型       |
| :-------: | :-------------: | :-------------------: |
|  Series   | `series[label]` |         标量          |
| DataFrame |  `df[colname]`  | 对应colname的`Series` |



**:warning:在交换DataFrame的两列时，`loc`和`iloc`的表现不同**

**对于如下的DataFrame：**

```python
df = pd.DataFrame(np.arange(15).reshape((5, 3)),
                  index=list('abcde'),
                  columns=["A", "B", "C"])
print(df)

    A   B   C
a   0   1   2
b   3   4   5
c   6   7   8
d   9  10  11
e  12  13  14
```

**最简单的方式是原地交换，不使用`loc`或`iloc`，可以看到A B两列已经互换：**

```python
df[['B', 'A']] = df[['A', 'B']]
print(df)

    A   B   C
a   1   0   2
b   4   3   5
c   7   6   8
d  10   9  11
e  13  12  14
```



**:a:使用`loc`交换两列**

**当使用`loc`索引Series和DataFrame的时候，Pandas会<span style='color: red'>对齐所有</span>轴（Axes）**

```python
df.loc[:, ['B', 'A']] = df[['A', 'B']]
print(df)

    A   B   C
a   0   1   2
b   3   4   5
c   6   7   8
d   9  10  11
e  12  13  14
```

**可以看到两列的数据没有互换，这是因为在赋值之前，列标签已经对齐了**



**如果想使用`loc`进行两列互换，则使用`to_numpy`**

```python
df.loc[:, ['B', 'A']] = df[['A', 'B']].to_numpy()
print(df)

    A   B   C
a   1   0   2
b   4   3   5
c   7   6   8
d  10   9  11
e  13  12  14
```





**:b:使用`iloc`交换两列**

**然而，当使用`iloc`索引Series和DataFrame时，Pandas<span style='color: red'>不会对齐所有轴</span>，因为`iloc`是基于位置。**

```python
df.iloc[:, [1, 0]] = df[['A', 'B']]
print(df)

    A   B   C
a   1   0   2
b   4   3   5
c   7   6   8
d  10   9  11
e  13  12  14
```

**可以看到，A B 两列互换了，因为在赋值之前没有进行列标签对齐**





## 2、属性访问和修改

**你可以直接将Series的索引或DataFrame的列作为属性来看待，可以对其访问或修改。**

**如果你通过`.`的方式创建新的Series的索引或新的DataFrame的列，它不会添加新的数据，只会把它当作新属性来创建。**

**有几点需要注意：**

- **仅当索引元素是有效的Python标识符时，才可以使用此访问方式，例如`s.1`不允许**
- **如果属性与现有方法名称冲突，则该属性将不可用，例如`s.min`不允许，但`s['min']`可用**
- **同样，如果属性与以下列表任何一个冲突，则属性不可用：`index`, `major_axis`,  `minor_axis`, `items`**
- **在任何情况下，标准索引仍然有效，例如`s['1']`, `s['min']`，并且`s['index']`将会访问相应的元素或列**



```python
#Series的索引相当于Series的属性，可以通过 '.' 的方式来访问或修改
#Series.index，其返回值是一个标量
ser = pd.Series([1, 2, 3], index=list('abc'))
print(ser)
print(f"ser.a = {ser.a}")
ser.b = 6
print(ser)

#运行结果如下
a    1
b    2
c    3
dtype: int64
ser.a = 1
a    1
b    6
c    3
dtype: int64



#DataFrame的列标签相当于DataFrame的属性，可以通过 '.'的方式来访问或修改
#df.colname(等价于Python的obj.属性名) ，返回的是Pandas的Series对象
df = pd.DataFrame(np.arange(15).reshape((5, 3)),
                  index=list('abcde'),
                  columns=["A", "B", "C"])
print(df)
print("===========取DataFrame的A列============")
print(df.A)
print(f"df.A的类型: {type(df.A)}")
df.A = np.random.rand(5)
print(df)


#运行结果如下
    A   B   C
a   0   1   2
b   3   4   5
c   6   7   8
d   9  10  11
e  12  13  14
===========取DataFrame的A列============
a     0
b     3
c     6
d     9
e    12
Name: A, dtype: int64
df.A的类型: <class 'pandas.core.series.Series'>
          A   B   C
a  0.319460   1   2
b  0.575938   4   5
c  0.808036   7   8
d  0.241485  10  11
e  0.834912  13  14
```



**可以把一个字典赋值给DataFrame的某一行**

```python
df.iloc[1] = {'A': 5, 'B': 6, 'C': 7}
>>> print(df)

          A   B   C
a  0.319460   1   2
b  5.000000   6   7
c  0.808036   7   8
d  0.241485  10  11
e  0.834912  13  14
```





## 3、按callable选择

**`iloc`,`loc`或`[]`可以接受一个callable作为索引器**

```python
np.random.seed(3)
df = pd.DataFrame(np.random.randn(6, 4),
                   index=list('abcdef'),
                   columns=list('ABCD'))
>>> print(df)
          A         B         C         D
a  1.788628  0.436510  0.096497 -1.863493
b -0.277388 -0.354759 -0.082741 -0.627001
c -0.043818 -0.477218 -1.313865  0.884622
d  0.881318  1.709573  0.050034 -0.404677
e -0.545360 -1.546477  0.982367 -1.101068
f -1.185047 -0.205650  1.486148  0.236716


>>> print(df[lambda row: df["A"] > 0])

          A         B         C         D
a  1.788628  0.436510  0.096497 -1.863493
d  0.881318  1.709573  0.050034 -0.404677


>>> print(df.loc[:, lambda col: ['A', 'B']])
>>> print(df.iloc[:, lambda col: [0, 1]])			#两行的结果一样，一个iloc一个loc
          A         B
a  1.788628  0.436510
b -0.277388 -0.354759
c -0.043818 -0.477218
d  0.881318  1.709573
e -0.545360 -1.546477
f -1.185047 -0.205650


>>> print(df.loc[:, lambda col: 'A'])	#返回Series
a    1.788628
b   -0.277388
c   -0.043818
d    0.881318
e   -0.545360
f   -1.185047
Name: A, dtype: float64


>>> print(df.loc[lambda row: ['c', 'e'], lambda col: 'A'])
>>> df1['A'].loc[lambda s: ['c', 'e']]			#两行等价
c   -0.043818
e   -0.545360
Name: A, dtype: float64
```





## 4、布尔索引

​	**使用布尔向量过滤数据，运算符包括`|`，`&`或`~`，这些运算符必须使用括号分组，因为运算优先级**

​	**对于`iloc`来说，当索引器为布尔值的Series时，会引发[ValueError][]，若仍想使用该Series，则使用`Series.values`作为索引器**



**:a:对于Series来说，完全相当于NumPy里的ndarray**

```python
In [162]: s = pd.Series(range(-3, 4))

In [163]: s
Out[163]: 
0   -3
1   -2
2   -1
3    0
4    1
5    2
6    3
dtype: int64

In [164]: s[s > 0]
Out[164]: 
4    1
5    2
6    3
dtype: int64

In [165]: s[(s < -1) | (s > 0.5)]
Out[165]: 
0   -3
1   -2
4    1
5    2
6    3
dtype: int64

In [166]: s[~(s < 0)]
Out[166]: 
3    0
4    1
5    2
6    3
dtype: int64
```



**:b:对于DataFrame进行布尔索引**

```python
df = pd.DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
                    'b': ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
                    'c': np.random.randn(7)})
>>> print(df)
       a  b         c
0    one  x -1.023785
1    one  y -0.712993
2    two  y  0.625245
3  three  x -0.160513
4    two  y -0.768836
5    one  x -0.230031
6    six  x  0.745056



#todo 现在想筛选在DataFrame的第一列中以t开头的每一行
mask = df['a'].map(lambda x: str(x).startswith('t'))
print(mask)
print(df[mask])


#输出结果如下
0    False
1    False
2     True
3     True
4     True
5    False
6    False
Name: a, dtype: bool
       a  b         c
2    two  y  0.625245
3  three  x -0.160513
4    two  y -0.768836


#使用多种方法选择数据
print(df.loc[(mask & (df['b'] == 'y')), 'b':'c'])
   b         c
2  y  0.625245
4  y -0.768836
```





:warning:**DataFrame的`iloc`不能直接使用布尔值的Series作为其索引器，只能通过`Series.values`实现索引**

```python
>>> df.iloc[mask.values]
       a  b         c
2    two  y  0.625245
3  three  x -0.160513
4    two  y -0.768836



>>> df.iloc[mask]
NotImplementedError: iLocation based boolean indexing on an integer type is not available
```





## # 特殊的例子

:one:**如果两者中至少有一个不存在，但索引已排序，并且可以与开始和停止标签进行比较，则切片仍将按预期工作，通过选择两者之间的排名标签：但是，如果两者中至少有一个不存在*，并且*索引未排序，则会引发错误**

```python
In [68]: s.sort_index()
Out[68]: 
0    a
2    c
3    b
4    e
5    d
dtype: object

In [69]: s.sort_index().loc[1:6]
Out[69]: 
2    c
3    b
4    e
5    d
dtype: object
```



**:two:重复索引不能作为切片的界限**

```python
s = pd.Series(list('abcdef'), index=[0, 3, 2, 5, 4, 2])
s.loc[2:5]
KeyError: 'Cannot get left slice bound for non-unique label: 2'
```



**:three:超出范围的[切片][]索引可以妥善处理**

```python
# these are allowed in Python/NumPy.
In [87]: x = list('abcdef')

In [88]: x
Out[88]: ['a', 'b', 'c', 'd', 'e', 'f']

In [89]: x[4:10]
Out[89]: ['e', 'f']

In [90]: x[8:10]
Out[90]: []

In [91]: s = pd.Series(x)

In [92]: s
Out[92]: 
0    a
1    b
2    c
3    d
4    e
5    f
dtype: object

In [93]: s.iloc[4:10]
Out[93]: 
4    e
5    f
dtype: object

In [94]: s.iloc[8:10]
Out[94]: Series([], dtype: object)
```



**:four:单个索引器超出返回会引发[IndexError][]**

```python
>>> dfl = pd.DataFrame(np.random.randn(5, 2), columns=list('AB'))
>>> dfl
Out[96]: 
          A         B
0 -0.082240 -2.182937
1  0.380396  0.084844
2  0.432390  1.519970
3 -0.493662  0.600178
4  0.274230  0.132885


>>> dfl.iloc[[4, 5, 6]]
IndexError: positional indexers are out-of-bounds

>>> dfl.iloc[:, 4]
IndexError: single positional indexer is out-of-bounds
```





**:five:如果设置了DataFrame或Series的行/列索引名称，则会在控制台中显示**

```python
In [335]: index = pd.Index(list(range(5)), name='rows')

In [336]: columns = pd.Index(['A', 'B', 'C'], name='cols')

In [337]: df = pd.DataFrame(np.random.randn(5, 3), index=index, columns=columns)

In [338]: df
Out[338]: 
cols         A         B         C
rows                              
0     1.295989 -1.051694  1.340429
1    -2.366110  0.428241  0.387275
2     0.433306  0.929548  0.278094
3     2.154730 -0.315628  0.264223
4     1.126818  1.132290 -0.353310

In [339]: df['A']
Out[339]: 
rows
0    1.295989
1   -2.366110
2    0.433306
3    2.154730
4    1.126818
Name: A, dtype: float64
```



**:six:列表推导式作为索引器，速度慢**

```python
In [168]: df2 = pd.DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
   .....:                     'b': ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
   .....:                     'c': np.random.randn(7)})
   .....: 

#尽量使用布尔索引，使用列表推导式速度会很慢        
In [171]: df2[[x.startswith('t') for x in df2['a']]]
Out[171]: 
       a  b         c
2    two  y  0.041290
3  three  x  0.361719
4    two  y -0.238075
```





# 三、多索引/高级索引

## 1、多级索引

**创建MulitIndex对象**

```python
In [1]: arrays = [
   ...:     ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
   ...:     ["one", "two", "one", "two", "one", "two", "one", "two"],
   ...: ]
   ...: 

In [2]: tuples = list(zip(*arrays))

In [3]: tuples
Out[3]: 
[('bar', 'one'),
 ('bar', 'two'),
 ('baz', 'one'),
 ('baz', 'two'),
 ('foo', 'one'),
 ('foo', 'two'),
 ('qux', 'one'),
 ('qux', 'two')]

In [4]: index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])

In [5]: index
Out[5]: 
MultiIndex([('bar', 'one'),
            ('bar', 'two'),
            ('baz', 'one'),
            ('baz', 'two'),
            ('foo', 'one'),
            ('foo', 'two'),
            ('qux', 'one'),
            ('qux', 'two')],
           names=['first', 'second'])

In [6]: s = pd.Series(np.random.randn(8), index=index)

In [7]: s
Out[7]: 
first  second
bar    one       0.469112
       two      -0.282863
baz    one      -1.509059
       two      -1.135632
foo    one       1.212112
       two      -0.173215
qux    one       0.119209
       two      -1.044236
dtype: float64
```



**`get_level_values`：获取某个层级上的值**

**`swaplevel()`：交换两个层级**



## 2、分层索引

​	**通常，MultiIndex的键采用元组的形式，例如`df.loc[(level1, level2), colname]`**

​	**需要注意的是，在Pandas中，元组和列表作为索引器的处理方法并不相同，元组被解释为一个多级键，而列表用于指定多个键，换句话说，元组水平移动（遍历层级）， 而列表垂直移动（扫描层级）**



**接下来基于下面的DataFrame做多层索引操作**

```python
col_index = list("ABC")
a = ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux']
b = ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']
row_Mindex = pd.MultiIndex.from_tuples(list(zip(a, b)), names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 3), index=row_Mindex, columns=col_index)
print(df)

#输出结果
                     A         B         C
first second                              
bar   one    -1.203815 -1.117614 -0.037679
      two     0.716182  0.990181  0.619420
baz   one     0.270049  1.229481  1.048383
      two    -1.094085  0.048565  0.523119
foo   one    -0.682122  0.045659  1.120481
      two     1.690086  0.367056 -0.457166
qux   one     0.447699 -0.933020  1.205719
      two    -0.388487 -0.262779  1.968220
```



**下面是多级索引**

```python
==============df.loc['bar']=====================
               A         B         C
second                              
one    -1.203815 -1.117614 -0.037679
two     0.716182  0.990181  0.619420
==============df.loc['bar': 'foo']=====================
                     A         B         C
first second                              
bar   one    -1.203815 -1.117614 -0.037679
      two     0.716182  0.990181  0.619420
baz   one     0.270049  1.229481  1.048383
      two    -1.094085  0.048565  0.523119
foo   one    -0.682122  0.045659  1.120481
      two     1.690086  0.367056 -0.457166
==============df.loc[('bar', 'one')]=====================
A   -1.203815
B   -1.117614
C   -0.037679
Name: (bar, one), dtype: float64
==============df.loc[('bar', 'one'), ]=====================
A   -1.203815
B   -1.117614
C   -0.037679
Name: (bar, one), dtype: float64
==============df.loc[('bar', 'one'), 'B']=====================
-1.1176140229590275
==============df.loc[('bar', 'one'):('baz', 'two')]=====================
                     A         B         C
first second                              
bar   one    -1.203815 -1.117614 -0.037679
      two     0.716182  0.990181  0.619420
baz   one     0.270049  1.229481  1.048383
      two    -1.094085  0.048565  0.523119
==============df.loc[('bar', 'one'):'foo']=====================
                     A         B         C
first second                              
bar   one    -1.203815 -1.117614 -0.037679
      two     0.716182  0.990181  0.619420
baz   one     0.270049  1.229481  1.048383
      two    -1.094085  0.048565  0.523119
foo   one    -0.682122  0.045659  1.120481
      two     1.690086  0.367056 -0.457166
==============df.loc[[('bar', 'one'), ('foo', 'one')]] 列表套元组=====================
                     A         B         C
first second                              
bar   one    -1.203815 -1.117614 -0.037679
foo   one    -0.682122  0.045659  1.120481
==============df.loc[(['bar', 'foo'], ['one', 'one']), ] 元组套列表=====================
                     A         B         C
first second                              
bar   one    -1.203815 -1.117614 -0.037679
foo   one    -0.682122  0.045659  1.120481
```



## 3、`take`——基于位置索引

**==DataFrame.take(*indices, axis=0*)==**

​	**沿着某个轴查找给定位置索引的元素，indices必须是array_like，且索引可以为负，`-1`代表倒数第一个位置**



**还是基于此DataFrame**

```python
                     A         B         C
first second                              
bar   one    -1.203815 -1.117614 -0.037679
      two     0.716182  0.990181  0.619420
baz   one     0.270049  1.229481  1.048383
      two    -1.094085  0.048565  0.523119
foo   one    -0.682122  0.045659  1.120481
      two     1.690086  0.367056 -0.457166
qux   one     0.447699 -0.933020  1.205719
      two    -0.388487 -0.262779  1.968220
```



```python
==============df.take([0, 3])=====================
                     A         B         C
first second                              
bar   one    -1.203815 -1.117614 -0.037679
baz   two    -1.094085  0.048565  0.523119
==============df.take([-2, 1])=====================
                     A         B         C
first second                              
qux   one     0.447699 -0.933020  1.205719
bar   two     0.716182  0.990181  0.619420
==============df.take([1, 2], axis=1)=====================
                     B         C
first second                    
bar   one    -1.117614 -0.037679
      two     0.990181  0.619420
baz   one     1.229481  1.048383
      two     0.048565  0.523119
foo   one     0.045659  1.120481
      two     0.367056 -0.457166
qux   one    -0.933020  1.205719
      two    -0.262779  1.968220
```



**关于性能，由于`take`方法处理的输入范围较窄，因此它比花式索引更快。例如：**

```python
import random
a = np.random.randn(100000, 15)
indexs = np.arange(10000)
random.shuffle(indexs)
%timeit a[indexs]
%timeit a.take(indexs)

399 μs ± 8.69 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
40.5 μs ± 229 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)


ser = pd.Series(a[:, 1])
%timeit ser[indexs]
%timeit ser.take(indexs)

468 μs ± 4.82 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
84.5 μs ± 266 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)


df = pd.DataFrame(np.random.randn(100000, 15))
indexs = np.arange(20000)
random.shuffle(indexs)
%timeit df.iloc[indexs]
%timeit df.take(indexs)

1.04 ms ± 10.5 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
1.02 ms ± 5.37 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```





## 4、横截面（`xs()`）

**==DataFrame.xs(*key, axis=0, level=None, drop_level=True*)==**

​	**返回Series或DataFrame的横截面，它使用*key*参数来选择MultiIndex特定层级上的数据**



| 参数： |
| ------ |

**①key：label 或 label的元组**

​	**指定哪个或哪些标签作为索引器**

**②axis: {0 或 'index'，1 或 'columns'}，默认0**

​	**沿着哪个轴检索横截面**

**③level：object，默认为前n级（n=1 或 len(key)）**

​	**如果某个键部分包含在多索引中，需指明所使用的层级，层级可以通过标签或者位置来引用**

**④drop_level：bool，默认True**

​	**如果为False，则返回与自身具有相同级别的对象**



| 返回值： |
| -------- |

**:arrow_right:返回Series或DataFrame的横截面**



**基于此DataFrame**

```python
d = {'num_legs': [4, 4, 2, 2],
     'num_wings': [0, 0, 2, 2],
     'class': ['mammal', 'mammal', 'mammal', 'bird'],
     'animal': ['cat', 'dog', 'bat', 'penguin'],
     'locomotion': ['walks', 'walks', 'flies', 'walks']}
df = pd.DataFrame(data=d)
df = df.set_index(['class', 'animal', 'locomotion'])
print(df)


                           num_legs  num_wings
class  animal  locomotion                     
mammal cat     walks              4          0
       dog     walks              4          0
       bat     flies              2          2
bird   penguin walks              2          2
```



```python
==============df.xs('mammal')=====================
                   num_legs  num_wings
animal locomotion                     
cat    walks              4          0
dog    walks              4          0
bat    flies              2          2
==============df.xs(('mammal', 'cat', 'walks'))=====================
num_legs     4
num_wings    0
Name: (mammal, cat, walks), dtype: int64
==============df.xs('walks', level=2)=====================
                num_legs  num_wings
class  animal                      
mammal cat             4          0
       dog             4          0
bird   penguin         2          2
==============df.xs(('mammal', 'bat'), level=['class', 1])=====================
            num_legs  num_wings
locomotion                     
flies              2          2
==============df.xs('num_wings', axis=1)=====================
class   animal   locomotion
mammal  cat      walks         0
        dog      walks         0
        bat      flies         2
bird    penguin  walks         2
Name: num_wings, dtype: int64
```







# 四、IO操作

## 1、pickle：二进制文件

*<span style='font-size: 20px'>Pickle文件是：</span>*

- *一种二进制文件*
- *包含Python对象的序列化数据*
- *可以完整保存和恢复Python对象的结构和状态*
- *Python特有的数据格式（不适用于其他编程语言）*

**[示例pickle文件](G:\01作业\Pandas\0620文件读取练习)，yahoo_volume.pkl 和 yahoo_price.pkl**



### pandas.read_pickle

**==pandas.read_pickle(*filepath_or_buffer, compression='infer', storage_options=None*)==**

​	**从文件里加载已经序列化（pickled） 的 pandas对象，即从pickle文件里加载**



| 参数： |
| ------ |

**①filepath_or_buffer：str，path 对象或类文件对象**

​	**指定读取文件的路径**

**②compression: str 或 dict，默认'infer'**

​	**用于指定可以解压缩哪些磁盘数据，例如`tar`,`gz`,	`zip`等扩展名**

**③storage_options: dict, 可选**

​	**对特定存储连接有意义的额外选项，例如主机、端口、用户名、密码等**



| 返回值： |
| -------- |

**:arrow_right:与文件中存储的对象类型相同**





### DataFrame.to_pickle

**==DataFrame.to_pickle(*path, compression='infer', protocol=5, storage_options=None*)==**

​	**将对象转换为pickle文件**



| 参数： |
| ------ |

**①path: str，path 对象 或 类文件对象**

​	**输出pickle文件的路径**

**②compression: str 或 dit，默认'infer'**

​	**用于动态压缩输出数据，例如`zip`，`gzip`,`tar`等扩展名**

**③protocal: int**

​	**用于指示pickler应使用的协议**

**④storage_options: dict, 可选**

​	**对特定存储连接有意义的额外选项，例如主机、端口、用户名、密码等**



```python
original_df = pd.DataFrame({"foo": range(5), "bar": range(5, 10)})
print("=================原数据====================")
print(original_df)
original_df.to_pickle("./examples/dummy.pkl")
print("=================读取出来的数据====================")
print(pd.read_pickle("./examples/dummy.pkl"))


#输出结果如下，文件夹里多了一个pkl文件
=================原数据====================
   foo  bar
0    0    5
1    1    6
2    2    7
3    3    8
4    4    9
=================读取出来的数据====================
   foo  bar
0    0    5
1    1    6
2    2    7
3    3    8
4    4    9



#压缩
----------------------------------------------------------------------------------
original_df = pd.DataFrame({"foo": range(5), "bar": range(5, 10)})
print("=================原数据压缩====================")
print(original_df)
original_df.to_pickle("./examples/dummy.pkl", compression='tar')
print("=================读取压缩后的数据====================")
print(pd.read_pickle("./examples/dummy.pkl", compression='tar'))


#输出结果如下，文件夹里多了一个pkl文件，
#扩展名虽然没变，但是里面数据已经压缩，读取时不指定compression参数会引发UnpicklingError: could not find MARK
=================原数据压缩====================
   foo  bar
0    0    5
1    1    6
2    2    7
3    3    8
4    4    9
=================读取压缩后的数据====================
   foo  bar
0    0    5
1    1    6
2    2    7
3    3    8
4    4    9
```





## 2、CSV / 文本文件

### **# 示例数据：** ###

```json
positionId,positionName,industryLables,createTime,salary
6802721,数据分析,"['电商', '社交', 'SQL', '数据库', '数据运营', 'BI']",2020/3/16 11:00,37500
5204912,数据建模,[],2020/3/16 11:08,15000
6877668,数据分析,[],2020/3/16 10:33,3500
6496141,数据分析,['电商'],2020/3/16 10:10,45000
6467417,数据分析,[],2020/3/16 9:56,30000
6882347,数据分析,"['音乐', '直播', 'BI', '可视化', '数据库']",2020/3/16 9:54,50000
6841659,数据分析,['工具软件'],2020/3/16 9:41,30000
6764018,数据建模工程师,"['云计算', '大数据', 'Hadoop', 'Spark', 'MySQL', 'Oracle']",2020/3/16 11:18,35000
6458372,数据分析专家,"['电商', '广告营销', '数据分析', '数据运营']",2020/3/16 10:57,60000
6786904,数据分析师,"['企业服务', '大数据', 'Hive', '数据挖掘', '数据分析', 'SQLServer']",2020/3/16 11:18,40000
16804629,数据分析师,"['电商', '广告营销', '数据分析']",2020/3/16 10:57,30000
6847013,大数据分析工程师(J11108),[],2020/3/16 9:25,30000
6763962,数据分析工程师,"['云计算', '大数据', 'Oracle', 'Hadoop', 'Spark', 'MySQL']",2020/3/16 11:18,20000
6804489,资深数据分析师,"['电商', '数据分析']",2020/3/16 10:57,30000
6657285,数据分析师,[],2020/3/16 10:59,37500
6882983,产品运营（偏数据分析）,[],2020/3/16 10:59,27500
6486988,资深数据分析师（杭州）,[],2020/3/16 10:59,37500
5519962,大数据建模总监,"['大数据', '互联网金融']",2020/3/16 11:08,37500
5559894,数据建模专家-杭州-01546,"['银行', '互联网金融', '数据挖掘', 'Spark', '算法']",2020/3/16 11:17,30000
6702852,数据分析专家（游戏业务）,"['游戏', '数据分析']",2020/3/16 10:19,37500
```



### pandas.read_csv

*pandas 读csv 默认类型推断*

   - 整列都是数字 → 自动变 int/float
   - 整列都是数字和空值 -> 自动变float
   - 混有文本 → 退化为 object
   - True/true/TRUE false/False/FALSE -> 布尔类型



*其参数分为以下几类：*

#### 1、基本参数

**①filepath_or_buffer**

​	**可以是文件路径，URL（包括http，ftp，S3定位）或者任意具有`read()`方法的对象（例如打开的文件或`StringIO`）**

**②sep: str, 默认为`,`for`read_csv()`, `\t`for`read_table()`**

​	**要使用的分隔符**

**③delimiter: str, 默认None**

​	**sep的替代参数名称**

**④delim_whitespace: 布尔值，默认False**

​	**指定是否使用空格作为分隔符，相当于设置`sep='\s+'`，如果为True，delimiter不需要传任何参数**



```python
testPath = "examples/test.csv"
#下面三行等效
pd.read_csv(testPath, sep=',')
pd.read_csv(testPath, sep=',')
pd.read_csv(testPath, delimiter=',')



#从buffer中读取，指定不同分隔符
from io import StringIO
testStr = """a|b|c|d|message
1|2|3|4|hello
5|6|7|8|world
9|10|11|12|foo"""
csv_text_buffer1 = StringIO(testStr)
pd.read_csv(csv_text_buffer1, sep='|')

str_space_sep = testStr.replace('|', ' ')
csv_text_buffer2 = StringIO(str_space_sep)
pd.read_csv(csv_text_buffer2, sep='\s+')
```



#### 2、列和索引的位置及名称

**①header：int或int列表，默认’infer‘**

​	**指定文件里的哪行作为DataFrame的列名**

**②names：array_like，默认None**

​	**要使用的列名列表，列表中的名称不能出现重复项。如果文件没有表头，则应该显示传递`header=None`**

**③index_col：int， str，int/str 序列或False, 可选，默认None**

​	**指定用作DataFrame的行标签的列，如果是给出int/str序列，则使用多级索引。默认`None`指定Pandas进行猜测**

**④usecols：列表或 callable，默认None**

​	**指定哪些列要被读取出来**



```python
pd.read_csv(testPath, usecols=['positionId', 'positionName'])	#只读两列
pd.read_csv(testPath, index_col=['positionId'])			#把positionId列作为DataFrame的行标签
pd.read_csv(testPath, header=0)							#第0行做表头
```





#### 3、常规解析配置

**①dtype：类型名或字典（列名: 类型名），默认None**

​	**数据的类型或每列的数据类型，例如`{'a': np.float64, 'b': np.int32, 'c': str}`**

**②engine: {'c', 'python', 'pyarrow'}**

​	**使用的解析器引擎，c和pyarrow引擎速度更快，而只有Python引擎支持多线程**

**③converters：字典，默认None**

​	**用于转换特定列中的函数字典，键是列名，值是callable**

**④true_values/false_values：列表，默认None**

​	**当作`True`/`False`的值的列表，两个参数需要一起使用**

**⑤skipinitialspace：布尔值，默认False**

​	**是否跳过分隔符后的空格**

**⑥skiprows：列表、整数或callable， 默认None**

​	**如果为整数，则表示跳过前skiprows行，如果为列表，则跳过某几行，如果为callable，则跳过返回值为True的几行**

**⑦skipfooter：int，默认0**

​	**文件底部要跳过的行数（不支持`engine='c'`）**

**⑧nrows： int， 默认None**

​	**要读取的文件行数**

**⑨low_memory: bool，默认True**

​	**是否降低内存占用**

**⑩memory_map：bool，默认False**

​	**如果提供了文件路径，则将文件对象直接映射到内存，并直接从内存中访问数据**



```python
#修改数据类型
pd.read_csv(testPath, dtype={
    'positionId': str,
    'salary': np.float64
})
# 跳过前5行读取
pd.read_csv(testPath, skiprows=5)
# 只读取奇数行的数据，重新指定列名
colname = ['positionId', 'positionName', 'industryLables', 'createTime, salary']
pd.read_csv(testPath, skiprows=lambda x: x % 2 == 0, header=None, names=colname)
# 读取文件的前8行
pd.read_csv(testPath, nrows=8)
# 使用python引擎
pd.read_csv(testPath, engine='python')
```



**自定义数据类型转换，使用converters参数**

```python
csv_txt = StringIO("""
id,price,on_sale
001,12.50,TRUE
002,8.99,FALSE
003,5.33,yes
004,,no
""")
pd.read_csv(csv_txt, converters={
    "on_sale": lambda x: str(x).strip().lower() in ['true', 'yes', '1']
})

   id  price  on_sale
0   1  12.50     True
1   2   8.99    False
2   3   5.33     True
3   4    NaN    False
```



**对于`true_values`和`false_values`，一起使用才生效**

```python
testStr = """response
Yes
No
N/A
1
0"""
a = pd.read_csv(StringIO(testStr), true_values=["Yes", "1"],
    false_values=["No", "0"])
print(a)
```





#### 4、缺失值处理

**①na_values：标量，str，列表 或 字典**

​	**指定把某个/些值当作Na/NaN的字符串，如果传递了字典，则可指定每列特定的缺失值**

**②keep_default_na：bool，默认为True**

​	**读取数据时是否包含默认的NaN值，根据`na_values`传入，行为如下：**

- **如果`keep_default_na`为True，且`na_values`被指定，则`na_values`指定的值也会被解析为NaN**
- **如果`keep_default_na`为True，且`na_values`未指定，则仅仅把默认的缺失值解析为NaN**
- **如果`keep_default_na`为False，且`na_values`被指定，则仅仅把`na_values`指定的值解析为NaN**
- **如果`keep_default_na`为False，且`na_values`未指定，则不会将任何字符串解析为NaN**

**请注意：如果`na_filter = False`，`keep_default_na`和`na_values`参数会被忽略**

**③na_filter：bool，默认True**

​	**是否检测缺失值（空字符串和na_values的值），默认检测。**

**对于没有任何NA的数据，传递`na_filter = false`可以提高读取大文件的性能**

**⑤skip_blank_lines: bool，默认True**

​	**如果为True， 则跳过空行；如果为False，空行里的数据均被解析为NaN**



```python
textStr = """
a,b,c,d,message
1,2,3,4,no
5,6,,8,world
9,0,11,12,foo
"""
str_buffer = StringIO(textStr)

#直接读取，只会把默认的缺失值当作NaN
>>> pd.read_csv(str_buffer)
   a  b     c   d message
0  1  2   3.0   4      no
1  5  6   NaN   8   world
2  9  0  11.0  12     foo


#指定被当作NaN的值
>>> pd.read_csv(str_buffer, na_values=['0', 'no'])  			#这两行等价
#   pd.read_csv(str_buffer, na_values=['0', 'no'], keep_default_na=True)

   a    b     c   d message
0  1  2.0   3.0   4     NaN
1  5  6.0   NaN   8   world
2  9  NaN  11.0  12     foo

#如果keep_default_na=False
>>> pd.read_csv(str_buffer, keep_default_na=False)
   a  b   c   d message
0  1  2   3   4      no
1  5  6       8   world
2  9  0  11  12     foo


#如果不使用默认的缺失值，又指定了na_values的话，会将na_values指定的值视为NaN
>>> pd.read_csv(str_buffer,na_values=['0', ''], keep_default_na=False)
   a    b     c   d message
0  1  2.0   3.0   4      no
1  5  6.0   NaN   8   world
2  9  NaN  11.0  12     foo


#如果na_filter = False,则na_values和keep_default_na设置的参数全部失效
>>> pd.read_csv(str_buffer,na_values=['0', 'no'], keep_default_na=True, na_filter=False)
   a  b   c   d message
0  1  2   3   4      no
1  5  6       8   world
2  9  0  11  12     foo


#na_values传dict，指定每一列的缺失值是什么
>>> pd.read_csv(str_buffer,na_values={
    'b': 0,
    'c': '',
    'message': 'foo'
})
   a    b     c   d message
0  1  2.0   3.0   4      no
1  5  6.0   NaN   8   world
2  9  NaN  11.0  12     NaN
```





#### 5、日期处理

**①parse_dates：bool，整数列表，列表嵌套列表，字典，默认False**

- **`True` -> 尝试解析索引**
- **`[1, 2, 3]` - > 将1、2、3列分别解析为单独的日期列**
- **`{'foo': [1, 3]}` - > 将1、 3列解析为日期并调用'foo'的结果**

**②keep_date_col: bool，默认False**

​	**如果为True且parse_dates指定多列组合，则会保留原始列**

**③date_format：str 或 字典（colname: format）, 默认None**

​	**如果与`parse_dates`一起使用，将根据此格式解析日期**

**④dayfirst: bool，默认False**

​	**DD/MM格式日期**

**⑤cache_dates: bool,默认True**

​	**如果为True，则使用唯一且已转换日期的缓存来应用日期时间转换，解析重复的日期字符串时会显著提高速度**





```python
#指定用  %Y-%m-%d %H:%M:%S 格式解析createTime列
testPath = "examples/test.csv"
pd.read_csv(testPath, usecols=['positionName', 'createTime'], parse_dates=['createTime'], date_format="%Y-%m-%d %H:%M:%S")
        positionName       createTime
0               数据分析  2020/3/16 11:00
1               数据建模  2020/3/16 11:08
2               数据分析  2020/3/16 10:33
3               数据分析  2020/3/16 10:10
4               数据分析   2020/3/16 9:56
5               数据分析   2020/3/16 9:54
6               数据分析   2020/3/16 9:41
7            数据建模工程师  2020/3/16 11:18
8             数据分析专家  2020/3/16 10:57
9              数据分析师  2020/3/16 11:18
10             数据分析师  2020/3/16 10:57
11  大数据分析工程师(J11108)   2020/3/16 9:25
12           数据分析工程师  2020/3/16 11:18
13           资深数据分析师  2020/3/16 10:57
14             数据分析师  2020/3/16 10:59
15       产品运营（偏数据分析）  2020/3/16 10:59
16       资深数据分析师（杭州）  2020/3/16 10:59
17           大数据建模总监  2020/3/16 11:08
18   数据建模专家-杭州-01546  2020/3/16 11:17
19      数据分析专家（游戏业务）  2020/3/16 10:19




#以特定格式解析
dateStr = """
date,value
01/01/2023 9:18,100
06/29/2024 10:14,105
12/11/2024 11:15,110
"""
from datetime import datetime
dateStr_buffer = StringIO(dateStr)
>>> pd.read_csv(dateStr_buffer, parse_dates=['date'], date_format=lambda x: datetime.strptime(x, "%m/%d/%Y %H:%M:%S"))

               date  value
0   01/01/2023 9:18    100
1  06/29/2024 10:14    105
2  12/11/2024 11:15    110



#解析多列组合在一列中
dateStr = """
year,month,day,value
2023,1,1,100
2023,1,2,105
2023,1,4,110
"""
dateStr_buffer = StringIO(dateStr)
pd.read_csv(dateStr_buffer, parse_dates={'dateTime': ['year', 'month', 'day']})
    dateTime  value
0 2023-01-01    100
1 2023-01-02    105
2 2023-01-04    110

FutureWarning: Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated. Combine the desired columns with pd.to_datetime after parsing instead.
  print(pd.read_csv(dateStr_buffer, parse_dates={'dateTime': ['year', 'month', 'day']}))

```





#### 6、Iteration

**①iterator: bool，默认False**

​	**返回`TextFileReader`对象，该对象用于迭代或使用`get_chunk()`访问**

**②chunksize: int, 默认None**

​	**返回`TextFileReade`对象用于迭代，可用`next()`进行访问**



```python
#iterator = True
------------------------------------------------------------------
with pd.read_csv(testPath, usecols=['positionId','positionName','salary'], iterator=True) as reader:
    print(reader.get_chunk(5))
    
   positionId positionName  salary
0     6802721         数据分析   37500
1     5204912         数据建模   15000
2     6877668         数据分析    3500
3     6496141         数据分析   45000
4     6467417         数据分析   30000



#指定chunksize
------------------------------------------------------------------
#逐块读取
with pd.read_csv(testPath, usecols=['positionId','positionName','salary'], chunksize=5) as reader:
    print(f"返回的对象类型： {reader}")
    for row in reader:
        print(row)
        
        
#输出结果如下        
返回的对象类型： <pandas.io.parsers.readers.TextFileReader object at 0x000001C9D405C860>
   positionId positionName  salary
0     6802721         数据分析   37500
1     5204912         数据建模   15000
2     6877668         数据分析    3500
3     6496141         数据分析   45000
4     6467417         数据分析   30000
   positionId positionName  salary
5     6882347         数据分析   50000
6     6841659         数据分析   30000
7     6764018      数据建模工程师   35000
8     6458372       数据分析专家   60000
9     6786904        数据分析师   40000
    positionId      positionName  salary
10    16804629             数据分析师   30000
11     6847013  大数据分析工程师(J11108)   30000
12     6763962           数据分析工程师   20000
13     6804489           资深数据分析师   30000
14     6657285             数据分析师   37500
    positionId     positionName  salary
15     6882983      产品运营（偏数据分析）   27500
16     6486988      资深数据分析师（杭州）   37500
17     5519962          大数据建模总监   37500
18     5559894  数据建模专家-杭州-01546   30000
19     6702852     数据分析专家（游戏业务）   37500


#使用next读取，读取到最后会引发StopIteration
df = pd.read_csv(testPath, usecols=['positionId','positionName','salary'], chunksize=5)
>>> next(df)

   positionId positionName  salary
0     6802721         数据分析   37500
1     5204912         数据建模   15000
2     6877668         数据分析    3500
3     6496141         数据分析   45000
4     6467417         数据分析   30000
```



#### 7、引用、压缩、文件格式

**①compression:{`'infer'`, `'gzip'`, `'bz2'`, `'zip'`, `'xz'`, `'zstd'`, `None`, `dict`}, 默认 `'infer'`**

​	**用于读取某个压缩文件的格式**

**②thousands：str，默认None**

​	**千位分隔符，例如`1,000`**

**③decimal：str，默认`'.'`**

​	**识别为小数点的字符，例如，欧洲数据使用`','`**

**④float_precision：string, 默认None**

​	**指定C引擎应使用哪种转换器来处理浮点数，`None`表示普通转换器、`high`表示高精度转换器，`round_trip`表示往返转换器**

**⑤lineterminator：str（长度1），默认None**

​	**用于将文件分行的字符，仅适用于C解释器**

**⑥quotechar: str（长度1）**

​	**用于表示引用项的开始和结束的字符，引用项可以包含分隔符，但分隔符会被忽略**

**⑦comment: str，默认None**

​	**此参数必须是单个字符，如果该行的第一个字符与指定的参数匹配，则不读取该行，即把这行当作注释**

**⑧encoding: str，默认None**

​	**读写时使用的字符集编码**





#### 8、错误处理

**on_bad_lines: {'error', 'warn', 'skip'}，默认'error'**

​	**指定在遇到一个bad line（一个字段过多的行）所做的操作**

- **`error`： 引发[ParserError][]**
- **`warn`：打印警告并跳过该行**
- **`skip`：直接跳过该行**



```python
textStr = """
a,b,c,d
1,2,3,4,no
5,6,7,8,9,10
6,8,5,4,yes
"""
str_buffer = StringIO(textStr)

#默认报错
>>> pd.read_csv(str_buffer)
ParserError: Error tokenizing data. C error: Expected 5 fields in line 4, saw 6


#警告，但跳过该行并读取了下一行
>>> pd.read_csv(str_buffer, on_bad_lines='warn')
   a  b  c    d
1  2  3  4   no
6  8  5  4  yes
C:\Users\98445\AppData\Local\Temp\ipykernel_5668\3015557271.py:8: ParserWarning: Skipping line 4: expected 5 fields, saw 6     pd.read_csv(str_buffer, on_bad_lines='warn')


#跳过bad lin
>>> pd.read_csv(str_buffer, on_bad_lines='skip')
   a  b  c    d
1  2  3  4   no
6  8  5  4  yes
```



#### :arrow_right:返回值

**DataFrame或TextFileReader**



### DataFrame.to_csv

| 参数： |
| ------ |

- **`path_or_buf`：要写入的文件的字符串路径或文件对象，如果是文件对象，则必须使用`newline=''`**
- **`sep`：输出文件的字段分隔符（默认`','`）**
- **`na_rep`：缺失值的字符串表示形式，默认`''`**
- **`float_format`: 浮点数的格式字符串**
- **`columns`：要写入的列（默认None）**
- **`header`：是否写出表头（默认True）**
- **`index`：是否写入行索引名称（默认True）**
- **`index_label`：指定哪一列为索引列，默认为None**
- **`mode`：Python的写入模式，默认'w'**
- **`encoding`：编码集**
- **`lineterminator`：表示行结束的字符序列，默认`os.linsep`**
- **`quoting`：设置csv模块中的引用规则**
- **`quotechar`：用于引用字段的字符，默认`''`**
- **`doublequote`：在字段中控制`quotechar`的引用（默认为True）**
- **`escapechar`：用于转移`sep`和`quotechar`的字符**
- **`chunksize`：一次要写多少行**
- **`date_format`：对于datetime对象格式化字符串**





## 3、JSON

### # 示例数据：

​	**[示例JSON1](G:\01作业\Pandas\0620文件读取练习)，某基金数据.json**

​	**[示例JSON2](https://api.github.com/repos/pandas-dev/pandas/issues)，pandas issue**



### pandas.read_json

| 参数： |
| ------ |

- **`filepath_or_buffer`：文件句柄、StringIO或URL（http/ftp/S3或文件）**
- **`typ`：{‘frame’, ‘series’}，表示要恢复的对象类型，默认DataFrame**
- **`orient`：**
  - **Series：默认为index，允许传入`split, records, index`；索引必须唯一**
  - **DataFrame：默认为columns，可以传入 {`split`, `records`, `index`, `columns`, `values`, `table`}，index必须唯一**

| orient参数 |                       JSON字符串的格式                       |
| :--------: | :----------------------------------------------------------: |
|  `split`   | 字典 {columns -> [columns], index -> [index], data -> [values]} |
| `records`  |                 列表[{column -> value} ...]                  |
|  `index`   |               字典{index -> {column -> value}}               |
| `columns`  |               字典{column -> {index -> value}}               |
|  `values`  |                        仅仅是值的数组                        |
|  `table`   |                     符合JSON的table格式                      |

- **`dtype`：bool或字典，默认为None。如果为True，则推断dtypes，否则不推断**
- **`convert_axes`：bool， 尝试将轴转换为正确的数据类型，默认为True**
- **`convert_dates`：bool或str的列表。指定要解析为日期的列的列表，如果为True，则尝试解析类似日期的列，默认为True**
- **`keep_default_dates`：bool， 默认为True**
- **`precise_float`：bool，默认为False，如果为True，则使用更高精度的数据类型进行解析数据**
- **`date_unit`：string， 用于检测是否需要转换日期的时间戳单位**
- **`lines`：每行读取一个JSON对象**
- **`encoding`：编码集， 默认'utf-8'**
- **`encoding_errors`：str,可选，默认strict**
- **`chunksize`：int, 可选。当和`lines=True`一起使用时，返回一个JsonReader对象用于迭代**
- **`compression`：str或dict，默认'infer'，指定可以读取哪些压缩文件**
- **`engine`：{'ujson', 'pyarrow'}，默认'ujson'。读取文件使用的引擎**
- **`nrows`：int， 可选，仅仅是`lines=True`的时候发挥作用**
- **`storage_options`：额外的存储选项**
- **`dtype_backend`：{'numpy_nullable', 'pyarrow'}, 默认'numpy_nullable'**



| 返回值 |
| ------ |

**:arrow_right:返回Series、DataFrame或pandas.api.typing.JsonReader对象**





```python
json_filepath = "./examples/某基金数据.json"
df = pd.read_json(json_filepath)
print(df.loc[:5])					#只读前五行数据


         净值日期   单位净值   累计净值    日增长率  申购状态  赎回状态  分红送配
0  2020-02-13  1.884  1.884  -0.11%  开放申购  开放赎回   NaN
1  2020-02-12  1.886  1.886   3.34%  开放申购  开放赎回   NaN
2  2020-02-11  1.825  1.825  -0.16%  开放申购  开放赎回   NaN
3  2020-02-10  1.828  1.828   1.33%  开放申购  开放赎回   NaN
4  2020-02-07  1.804  1.804   0.61%  开放申购  开放赎回   NaN
```





### Series/DataFrame.to_json

​	**把Series/DataFrame对象转为JSON字符串**

| 参数： |
| ------ |

**①path_or_buf：str, path对象，文件对象或None，默认None**

​	**指定输出JSON字符串的文件路径，如果为None，则返回str**

**②orient：str**

​	**对于Series，默认index，即`{index -> {column -> value}}`**

​	**对于DataFrame，默认columns，即`{column -> {index -> value}}`**

​	**其他参数参考 `pandas.read_json` 的 orient参数**

**③date_format：{None, 'epoch', 'iso'}**

​	**日期转换的类型**

**④force_ascii：bool，默认True**

​	**强制使用ASCII字符集编码**

**⑤default_handler：callable, 默认None**

​	**对不能解析为JSON字符串做某些处理**

**⑥compression：str或字典，默认'infer'**

​	**指定输出数据的压缩形式**

**⑦mode：str，默认'w'**

​	**指定输出模式**



| 返回值： |
| -------- |

**:arrow_right:返回None或str**

[详细参阅]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html



### **# 示例：** ###

**导入sys模块，将转换的 JSON 输出到控制台**

```python
df.to_json("./examples/out.json", force_ascii=False)		#带有中文的JSON需指定force_ascii = False


import sys
>>> df.loc[:5].to_json(sys.stdout, force_ascii=False)
{"净值日期":{"0":"2020-02-13","1":"2020-02-12","2":"2020-02-11","3":"2020-02-10","4":"2020-02-07","5":"2020-02-06"},"单位净值":{"0":1.884,"1":1.886,"2":1.825,"3":1.828,"4":1.804,"5":1.793},"累计净值":{"0":1.884,"1":1.886,"2":1.825,"3":1.828,"4":1.804,"5":1.793},"日增长率":{"0":"-0.11%","1":"3.34%","2":"-0.16%","3":"1.33%","4":"0.61%","5":"3.11%"},"申购状态":{"0":"开放申购","1":"开放申购","2":"开放申购","3":"开放申购","4":"开放申购","5":"开放申购"},"赎回状态":{"0":"开放赎回","1":"开放赎回","2":"开放赎回","3":"开放赎回","4":"开放赎回","5":"开放赎回"},"分红送配":{"0":null,"1":null,"2":null,"3":null,"4":null,"5":null}}
```





**下面使用`orient`参数来输出不同格式的字符串**

**:zero:首先将JSON文件转换为对应的DataFrame**

```python
json_filepath = "./examples/某基金数据.json"
df = pd.read_json(json_filepath, encoding='utf-8')
print(df)

         净值日期   单位净值   累计净值    日增长率  申购状态  赎回状态  分红送配
0  2020-02-13  1.884  1.884  -0.11%  开放申购  开放赎回   NaN
1  2020-02-12  1.886  1.886   3.34%  开放申购  开放赎回   NaN
2  2020-02-11  1.825  1.825  -0.16%  开放申购  开放赎回   NaN
3  2020-02-10  1.828  1.828   1.33%  开放申购  开放赎回   NaN
4  2020-02-07  1.804  1.804   0.61%  开放申购  开放赎回   NaN
5  2020-02-06  1.793  1.793   3.11%  开放申购  开放赎回   NaN
6  2020-02-05  1.739  1.739   1.64%  开放申购  开放赎回   NaN
7  2020-02-04  1.711  1.711   7.34%  开放申购  开放赎回   NaN
8  2020-02-03  1.594  1.594  -7.22%  开放申购  开放赎回   NaN
9  2020-01-23  1.718  1.718  -2.05%  开放申购  开放赎回   NaN
```



**:one:orient = split，即`{columns -> [columns], index -> [index], data -> [values]}`**

```python
import json
json_str = df.loc[:3].to_json(orient="split", force_ascii=False)
py_obj = json.loads(json_str)
print(json.dumps(py_obj, ensure_ascii=False, indent=4))		#有中文，所以不用ASCII编码


#输出结果如下
{
    "columns": [
        "净值日期",
        "单位净值",
        "累计净值",
        "日增长率",
        "申购状态",
        "赎回状态",
        "分红送配"
    ],
    "index": [
        0,
        1,
        2,
        3
    ],
    "data": [
        [
            "2020-02-13",
            1.884,
            1.884,
            "-0.11%",
            "开放申购",
            "开放赎回",
            null
        ],
        [
            "2020-02-12",
            1.886,
            1.886,
            "3.34%",
            "开放申购",
            "开放赎回",
            null
        ],
        [
            "2020-02-11",
            1.825,
            1.825,
            "-0.16%",
            "开放申购",
            "开放赎回",
            null
        ],
        [
            "2020-02-10",
            1.828,
            1.828,
            "1.33%",
            "开放申购",
            "开放赎回",
            null
        ]
    ]
}
```





**:two:orient = records， 即`[{column -> value}...]`**

```python
json_str = df.to_json(orient="records", force_ascii=False)
py_obj = json.loads(json_str)
print(json.dumps(py_obj, ensure_ascii=False, indent=4))

[
    {
        "净值日期": "2020-02-13",
        "单位净值": 1.884,
        "累计净值": 1.884,
        "日增长率": "-0.11%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    {
        "净值日期": "2020-02-12",
        "单位净值": 1.886,
        "累计净值": 1.886,
        "日增长率": "3.34%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    {
        "净值日期": "2020-02-11",
        "单位净值": 1.825,
        "累计净值": 1.825,
        "日增长率": "-0.16%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    {
        "净值日期": "2020-02-10",
        "单位净值": 1.828,
        "累计净值": 1.828,
        "日增长率": "1.33%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    {
        "净值日期": "2020-02-07",
        "单位净值": 1.804,
        "累计净值": 1.804,
        "日增长率": "0.61%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    {
        "净值日期": "2020-02-06",
        "单位净值": 1.793,
        "累计净值": 1.793,
        "日增长率": "3.11%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    {
        "净值日期": "2020-02-05",
        "单位净值": 1.739,
        "累计净值": 1.739,
        "日增长率": "1.64%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    {
        "净值日期": "2020-02-04",
        "单位净值": 1.711,
        "累计净值": 1.711,
        "日增长率": "7.34%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    {
        "净值日期": "2020-02-03",
        "单位净值": 1.594,
        "累计净值": 1.594,
        "日增长率": "-7.22%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    {
        "净值日期": "2020-01-23",
        "单位净值": 1.718,
        "累计净值": 1.718,
        "日增长率": "-2.05%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    }
]
```





**:three:orient = values，仅仅是值的数组**

```python
json_str = df.to_json(orient="values", force_ascii=False)
py_obj = json.loads(json_str)
print(json.dumps(py_obj, ensure_ascii=False, indent=4))


[
    [
        "2020-02-13",
        1.884,
        1.884,
        "-0.11%",
        "开放申购",
        "开放赎回",
        null
    ],
    [
        "2020-02-12",
        1.886,
        1.886,
        "3.34%",
        "开放申购",
        "开放赎回",
        null
    ],
    [
        "2020-02-11",
        1.825,
        1.825,
        "-0.16%",
        "开放申购",
        "开放赎回",
        null
    ],
    [
        "2020-02-10",
        1.828,
        1.828,
        "1.33%",
        "开放申购",
        "开放赎回",
        null
    ],
    [
        "2020-02-07",
        1.804,
        1.804,
        "0.61%",
        "开放申购",
        "开放赎回",
        null
    ],
    [
        "2020-02-06",
        1.793,
        1.793,
        "3.11%",
        "开放申购",
        "开放赎回",
        null
    ],
    [
        "2020-02-05",
        1.739,
        1.739,
        "1.64%",
        "开放申购",
        "开放赎回",
        null
    ],
    [
        "2020-02-04",
        1.711,
        1.711,
        "7.34%",
        "开放申购",
        "开放赎回",
        null
    ],
    [
        "2020-02-03",
        1.594,
        1.594,
        "-7.22%",
        "开放申购",
        "开放赎回",
        null
    ],
    [
        "2020-01-23",
        1.718,
        1.718,
        "-2.05%",
        "开放申购",
        "开放赎回",
        null
    ]
]
```





**:four:orient = table，符合JSON的表格格式, 格式如下 `**

```python
{
    "schema": {
        "fields": [{name -> fieldName, type -> fieldType} ...],
        "primaryKey": ["index"],
        "pandas_version": version
    },
    "data":[{
        "index": indexName,
        "column1": data1,
        "column2": data2,
        ...
    },{
        "index": indexName,
        "column1": data1,
        "column2": data2,
        ...
    }
    ...    
    ]
}
```



**示例：**

```python
json_str = df.to_json(orient="table", force_ascii=False)
py_obj = json.loads(json_str)
print(json.dumps(py_obj, ensure_ascii=False, indent=4))

{
    "schema": {
        "fields": [
            {
                "name": "index",
                "type": "integer"
            },
            {
                "name": "净值日期",
                "type": "string"
            },
            {
                "name": "单位净值",
                "type": "number"
            },
            {
                "name": "累计净值",
                "type": "number"
            },
            {
                "name": "日增长率",
                "type": "string"
            },
            {
                "name": "申购状态",
                "type": "string"
            },
            {
                "name": "赎回状态",
                "type": "string"
            },
            {
                "name": "分红送配",
                "type": "number"
            }
        ],
        "primaryKey": [
            "index"
        ],
        "pandas_version": "1.4.0"
    },
    "data": [
        {
            "index": 0,
            "净值日期": "2020-02-13",
            "单位净值": 1.884,
            "累计净值": 1.884,
            "日增长率": "-0.11%",
            "申购状态": "开放申购",
            "赎回状态": "开放赎回",
            "分红送配": null
        },
        {
            "index": 1,
            "净值日期": "2020-02-12",
            "单位净值": 1.886,
            "累计净值": 1.886,
            "日增长率": "3.34%",
            "申购状态": "开放申购",
            "赎回状态": "开放赎回",
            "分红送配": null
        },
        {
            "index": 2,
            "净值日期": "2020-02-11",
            "单位净值": 1.825,
            "累计净值": 1.825,
            "日增长率": "-0.16%",
            "申购状态": "开放申购",
            "赎回状态": "开放赎回",
            "分红送配": null
        },
        {
            "index": 3,
            "净值日期": "2020-02-10",
            "单位净值": 1.828,
            "累计净值": 1.828,
            "日增长率": "1.33%",
            "申购状态": "开放申购",
            "赎回状态": "开放赎回",
            "分红送配": null
        },
        {
            "index": 4,
            "净值日期": "2020-02-07",
            "单位净值": 1.804,
            "累计净值": 1.804,
            "日增长率": "0.61%",
            "申购状态": "开放申购",
            "赎回状态": "开放赎回",
            "分红送配": null
        },
        {
            "index": 5,
            "净值日期": "2020-02-06",
            "单位净值": 1.793,
            "累计净值": 1.793,
            "日增长率": "3.11%",
            "申购状态": "开放申购",
            "赎回状态": "开放赎回",
            "分红送配": null
        },
        {
            "index": 6,
            "净值日期": "2020-02-05",
            "单位净值": 1.739,
            "累计净值": 1.739,
            "日增长率": "1.64%",
            "申购状态": "开放申购",
            "赎回状态": "开放赎回",
            "分红送配": null
        },
        {
            "index": 7,
            "净值日期": "2020-02-04",
            "单位净值": 1.711,
            "累计净值": 1.711,
            "日增长率": "7.34%",
            "申购状态": "开放申购",
            "赎回状态": "开放赎回",
            "分红送配": null
        },
        {
            "index": 8,
            "净值日期": "2020-02-03",
            "单位净值": 1.594,
            "累计净值": 1.594,
            "日增长率": "-7.22%",
            "申购状态": "开放申购",
            "赎回状态": "开放赎回",
            "分红送配": null
        },
        {
            "index": 9,
            "净值日期": "2020-01-23",
            "单位净值": 1.718,
            "累计净值": 1.718,
            "日增长率": "-2.05%",
            "申购状态": "开放申购",
            "赎回状态": "开放赎回",
            "分红送配": null
        }
    ]
}
```



**:five:orient = index，即`{index -> {column -> value}}`，Series默认**

```python
json_str = df.to_json(orient="index", force_ascii=False)
py_obj = json.loads(json_str)
print(json.dumps(py_obj, ensure_ascii=False, indent=4))

{
    "0": {
        "净值日期": "2020-02-13",
        "单位净值": 1.884,
        "累计净值": 1.884,
        "日增长率": "-0.11%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    "1": {
        "净值日期": "2020-02-12",
        "单位净值": 1.886,
        "累计净值": 1.886,
        "日增长率": "3.34%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    "2": {
        "净值日期": "2020-02-11",
        "单位净值": 1.825,
        "累计净值": 1.825,
        "日增长率": "-0.16%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    "3": {
        "净值日期": "2020-02-10",
        "单位净值": 1.828,
        "累计净值": 1.828,
        "日增长率": "1.33%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    "4": {
        "净值日期": "2020-02-07",
        "单位净值": 1.804,
        "累计净值": 1.804,
        "日增长率": "0.61%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    "5": {
        "净值日期": "2020-02-06",
        "单位净值": 1.793,
        "累计净值": 1.793,
        "日增长率": "3.11%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    "6": {
        "净值日期": "2020-02-05",
        "单位净值": 1.739,
        "累计净值": 1.739,
        "日增长率": "1.64%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    "7": {
        "净值日期": "2020-02-04",
        "单位净值": 1.711,
        "累计净值": 1.711,
        "日增长率": "7.34%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    "8": {
        "净值日期": "2020-02-03",
        "单位净值": 1.594,
        "累计净值": 1.594,
        "日增长率": "-7.22%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    },
    "9": {
        "净值日期": "2020-01-23",
        "单位净值": 1.718,
        "累计净值": 1.718,
        "日增长率": "-2.05%",
        "申购状态": "开放申购",
        "赎回状态": "开放赎回",
        "分红送配": null
    }
}
```



**:six:orient = columns，即`{column -> {index -> value}}`，DataFrame默认**

```python
json_str = df.to_json(orient="columns", force_ascii=False)
py_obj = json.loads(json_str)
print(json.dumps(py_obj, ensure_ascii=False, indent=4))

{
    "净值日期": {
        "0": "2020-02-13",
        "1": "2020-02-12",
        "2": "2020-02-11",
        "3": "2020-02-10",
        "4": "2020-02-07",
        "5": "2020-02-06",
        "6": "2020-02-05",
        "7": "2020-02-04",
        "8": "2020-02-03",
        "9": "2020-01-23"
    },
    "单位净值": {
        "0": 1.884,
        "1": 1.886,
        "2": 1.825,
        "3": 1.828,
        "4": 1.804,
        "5": 1.793,
        "6": 1.739,
        "7": 1.711,
        "8": 1.594,
        "9": 1.718
    },
    "累计净值": {
        "0": 1.884,
        "1": 1.886,
        "2": 1.825,
        "3": 1.828,
        "4": 1.804,
        "5": 1.793,
        "6": 1.739,
        "7": 1.711,
        "8": 1.594,
        "9": 1.718
    },
    "日增长率": {
        "0": "-0.11%",
        "1": "3.34%",
        "2": "-0.16%",
        "3": "1.33%",
        "4": "0.61%",
        "5": "3.11%",
        "6": "1.64%",
        "7": "7.34%",
        "8": "-7.22%",
        "9": "-2.05%"
    },
    "申购状态": {
        "0": "开放申购",
        "1": "开放申购",
        "2": "开放申购",
        "3": "开放申购",
        "4": "开放申购",
        "5": "开放申购",
        "6": "开放申购",
        "7": "开放申购",
        "8": "开放申购",
        "9": "开放申购"
    },
    "赎回状态": {
        "0": "开放赎回",
        "1": "开放赎回",
        "2": "开放赎回",
        "3": "开放赎回",
        "4": "开放赎回",
        "5": "开放赎回",
        "6": "开放赎回",
        "7": "开放赎回",
        "8": "开放赎回",
        "9": "开放赎回"
    },
    "分红送配": {
        "0": null,
        "1": null,
        "2": null,
        "3": null,
        "4": null,
        "5": null,
        "6": null,
        "7": null,
        "8": null,
        "9": null
    }
}
```





## 4、Excel

### # 示例Excel

​	**[示例Excel](G:\01作业\Pandas\0620文件读取练习)，TOP250.xlsx**



**获取某个Excel的所有sheetName使用 `pd.ExcelFile(excel_file_path).sheet_names`**



### pandas.read_excel

​	**将Excel文件读取成Pandas的DataFrame**



| 参数： |
| ------ |

**①io：str, ExcelFile, xlrd.Book, path对象 或 类文件对象**

​	**要读取的Excel文件路径，可以是URL，URL包括http、ftp、s3和file**

**②sheet_name：str, int, list 或 None，默认0**

​	**指定读取哪个sheet（工作簿），图表的sheet不计入工作簿的位置**

- **默认为`0·，即读取第一个sheet**
- **`1`：读取第二个sheet，依此类推**
- **`"sheet1"`：加载名为"sheet1"的工作簿**
- **`[0, 1, "sheet5"]`：加载第一、第二和名为"sheet5"的工作簿，并把它们转为DataFrame的字典（键是sheetName，值是对应的DataFrame）**
- **`None`：读取所有工作表**

**③header：int，int列表，默认0**

​	**指定哪一行作为表头，如果传递的是整数列表，则被合并为多级索引**

**④names：数组，默认None**

​	**如果文件没有表头，则指定相应的names**

**⑤index_col：int，str，int列表，默认None**

​	**指定当作行索引的列**

**⑥usecols: str, 列表或callable, 默认None**

- **如果为None，则解析所有列**
- **如果为str，则使用Excel列的字母，例如`A:E`或`A,C,E,F`，范围包含两边**
- **如果为int列表，则表示要读取的列，下标从0开始**
- **如果为str列表，则列表内的str应该是列名**
- **如果是callable，则读取返回值为True的列**

**⑦dtype：数据类型或字典（column -> type）,默认None**

​	**指定某些列解析成什么数据类型，例如`{'a': np.float64, 'b': np.int32}`**

**⑧converters：字典，默认None**

​	**用于转换特定列中值的字典，键是列标签，值是callable，接受一个输入参数（Excel单元格的内容）**

**⑨skiprows：列表，int 或 callable，可选**

​	**指定要跳过的行，如果为int，则跳过前skiprows行，如果为列表或callable，则跳过指定的行**

**⑩nrows：int，默认None**

​	**指定要读取前几行**



| 返回值： |
| -------- |

**:arrow_right:DataFrame或包含多个DataFrame的字典**

[详情参阅]: https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html





### # read_excel示例

**:a:先来看读取Excel中的所有sheet（工作簿），需指定`sheet_name = None`，它返回一个字典（sheetName -> DataFrame）**

```python
>>> pd.read_excel(exc_file_path, sheet_name=None)

{'movie':            片名  上映年份   评分     评价人数        导演  \
 0      肖申克的救赎  1994  9.7  2317937  弗兰克·德拉邦特   
 1        霸王别姬  1993  9.6  1720638       陈凯歌   
 2        阿甘正传  1994  9.5  1743966  罗伯特·泽米吉斯   
 3     这个杀手不太冷  1994  9.4  1922740     吕克·贝松   
 4       泰坦尼克号  1997  9.4  1706127   詹姆斯·卡梅隆   
 ..        ...   ...  ...      ...       ...   
 245        浪潮  2008  8.7   223511   丹尼斯·甘塞尔   
 246  小萝莉的猴神大叔  2015  8.4   404886     卡比尔·汗   
 247        追随  1998  8.9   149521  克里斯托弗·诺兰   
 248      网络谜踪  2018  8.6   430811   阿尼什·查甘蒂   
 249      黑鹰坠落  2001  8.7   239402   雷德利·斯科特   
 
                                                编剧  \
 0                                弗兰克·德拉邦特 / 斯蒂芬·金   
 1                                        芦苇 / 李碧华   
 2                                艾瑞克·罗斯 / 温斯顿·格鲁姆   
 3                                           吕克·贝松   
 4                                         詹姆斯·卡梅隆   
 ..                                            ...   
 245  丹尼斯·甘塞尔 / 彼得·图万斯 / 约翰尼·道金斯 / 罗恩·比恩巴赫 / 罗恩·琼斯   
 246                            卡比尔·汗 / 维杰耶德拉·普拉萨德   
 247                                      克里斯托弗·诺兰   
 248                             阿尼什·查甘蒂 / 赛弗·奥哈尼安   
 249                                  肯·诺兰 / 马克·鲍登   
 
                                                     主演                 类型  \
 0    蒂姆·罗宾斯 / 摩根·弗里曼 / 鲍勃·冈顿 / 威廉姆·赛德勒 / 克兰西·布朗 / 吉...            剧情 / 犯罪   
 1    张国荣 / 张丰毅 / 巩俐 / 葛优 / 英达 / 蒋雯丽 / 吴大维 / 吕齐 / 雷汉...       剧情 / 爱情 / 同性   
 2    汤姆·汉克斯 / 罗宾·怀特 / 加里·西尼斯 / 麦凯尔泰·威廉逊 / 莎莉·菲尔德 / ...            剧情 / 爱情   
 3    让·雷诺 / 娜塔莉·波特曼 / 加里·奥德曼 / 丹尼·爱罗 / 彼得·阿佩尔 / 迈克尔...       剧情 / 动作 / 犯罪   
 4    莱昂纳多·迪卡普里奥 / 凯特·温丝莱特 / 比利·赞恩 / 凯西·贝茨 / 弗兰西丝·费舍...       剧情 / 爱情 / 灾难   
 ..                                                 ...                ...   
 245  于尔根·福格尔 / 弗雷德里克·劳 / 马克思·雷迈特 / 詹妮弗·乌尔里希 / 克里斯蒂安...            剧情 / 惊悚   
 246  萨尔曼·汗 / 哈莎莉·马洛特拉 / 卡琳娜·卡普尔 / 纳瓦祖丁·席迪圭 / 欧姆·普瑞 ...       剧情 / 喜剧 / 动作   
 247  杰里米·西奥伯德 / 亚历克斯·霍 / 露西·拉塞尔 / 约翰·诺兰 / 迪克·布拉德塞尔 ...       悬疑 / 惊悚 / 犯罪   
 248  约翰·赵 / 米切尔·拉 / 黛博拉·梅辛 / 约瑟夫·李 / 萨拉·米博·孙 / 亚历克丝...  剧情 / 悬疑 / 惊悚 / 犯罪   
 249  乔什·哈奈特 / 伊万·麦克格雷格 / 汤姆·塞兹摩尔 / 金·寇兹 / 艾文·布莱纳 / ...       动作 / 历史 / 战争   
 
     国家/地区     语言  时长(分钟)  
 0      美国     英语     142  
 1      中国  汉语普通话     171  
 2      美国     英语     142  
 3      法国    英语      110  
 4      美国    英语      194  
 ..    ...    ...     ...  
 245    德国     德语     107  
 246    印度   印地语      159  
 247    英国     英语      69  
 248    美国     英语     102  
 249    美国    英语      144  
 
 [250 rows x 11 columns],
 'scores':     student_id name  math  english  physics
 0        20001   朱七    51       64       71
 1        20002  冯思俊    63       83       62
 2        20003  赵志宇   100       86       82
 3        20004  秦八六    99       69       78
 4        20005   王嘉    87       57       92
 ..         ...  ...   ...      ...      ...
 95       20096   蒋欣    76       79       96
 96       20097   郑浩    52       71       66
 97       20098  赵豪思    60       50       64
 98       20099  韩琪宇    91       68       88
 99       20100  尤嘉俊    67       77       98
 
 [100 rows x 5 columns]}
```





**:b:再来分别读取每个表**

**读取第一个表，sheet_name=0 或 ‘movie’，默认读取第一个表**

```python
exc_file_path = "./examples/TOP250.xlsx"
print("=================不指定sheet_name 默认读第一个表=======================")
print("=================usecols = str_list [\"片名", "导演", "类型", "时长(分钟)\"] =======================")
print(pd.read_excel(exc_file_path, usecols=["片名", "导演", "类型", "时长(分钟)"]))
print("=================usecols = str 'A,B,E,K' =======================")
print(pd.read_excel(exc_file_path, usecols='A,B,E,K'))
print("=================usecols = str（切片形式）A:D =======================")
print(pd.read_excel(exc_file_path, usecols='A:D'))
print("=================usecols = callable  在[\"片名\", '评分', '好评', '导演']里面的 =======================")
print(pd.read_excel(exc_file_path, usecols=lambda x: x in ["片名", '评分', '好评', '导演']))


#输出结果如下
=================不指定sheet_name 默认读第一个表=======================
=================usecols = str_list ["片名 导演 类型 时长(分钟)"] =======================
           片名        导演                 类型  时长(分钟)
0      肖申克的救赎  弗兰克·德拉邦特            剧情 / 犯罪     142
1        霸王别姬       陈凯歌       剧情 / 爱情 / 同性     171
2        阿甘正传  罗伯特·泽米吉斯            剧情 / 爱情     142
3     这个杀手不太冷     吕克·贝松       剧情 / 动作 / 犯罪     110
4       泰坦尼克号   詹姆斯·卡梅隆       剧情 / 爱情 / 灾难     194
..        ...       ...                ...     ...
245        浪潮   丹尼斯·甘塞尔            剧情 / 惊悚     107
246  小萝莉的猴神大叔     卡比尔·汗       剧情 / 喜剧 / 动作     159
247        追随  克里斯托弗·诺兰       悬疑 / 惊悚 / 犯罪      69
248      网络谜踪   阿尼什·查甘蒂  剧情 / 悬疑 / 惊悚 / 犯罪     102
249      黑鹰坠落   雷德利·斯科特       动作 / 历史 / 战争     144

[250 rows x 4 columns]
=================usecols = str 'A,B,E,K' =======================
           片名  上映年份        导演  时长(分钟)
0      肖申克的救赎  1994  弗兰克·德拉邦特     142
1        霸王别姬  1993       陈凯歌     171
2        阿甘正传  1994  罗伯特·泽米吉斯     142
3     这个杀手不太冷  1994     吕克·贝松     110
4       泰坦尼克号  1997   詹姆斯·卡梅隆     194
..        ...   ...       ...     ...
245        浪潮  2008   丹尼斯·甘塞尔     107
246  小萝莉的猴神大叔  2015     卡比尔·汗     159
247        追随  1998  克里斯托弗·诺兰      69
248      网络谜踪  2018   阿尼什·查甘蒂     102
249      黑鹰坠落  2001   雷德利·斯科特     144

[250 rows x 4 columns]
=================usecols = str（切片形式）A:D =======================
           片名  上映年份   评分     评价人数
0      肖申克的救赎  1994  9.7  2317937
1        霸王别姬  1993  9.6  1720638
2        阿甘正传  1994  9.5  1743966
3     这个杀手不太冷  1994  9.4  1922740
4       泰坦尼克号  1997  9.4  1706127
..        ...   ...  ...      ...
245        浪潮  2008  8.7   223511
246  小萝莉的猴神大叔  2015  8.4   404886
247        追随  1998  8.9   149521
248      网络谜踪  2018  8.6   430811
249      黑鹰坠落  2001  8.7   239402

[250 rows x 4 columns]
=================usecols = callable  在["片名", '评分', '好评', '导演']里面的 =======================
           片名   评分        导演
0      肖申克的救赎  9.7  弗兰克·德拉邦特
1        霸王别姬  9.6       陈凯歌
2        阿甘正传  9.5  罗伯特·泽米吉斯
3     这个杀手不太冷  9.4     吕克·贝松
4       泰坦尼克号  9.4   詹姆斯·卡梅隆
..        ...  ...       ...
245        浪潮  8.7   丹尼斯·甘塞尔
246  小萝莉的猴神大叔  8.4     卡比尔·汗
247        追随  8.9  克里斯托弗·诺兰
248      网络谜踪  8.6   阿尼什·查甘蒂
249      黑鹰坠落  8.7   雷德利·斯科特

[250 rows x 3 columns]
```





**读取第二个表，sheet_name=1 或 'scores'**

```python
print("=================指定sheet_name = scores 读scores表=======================")
print(pd.read_excel(exc_file_path, sheet_name="scores"))
print("=================读scores表的前20行=======================")
print(pd.read_excel(exc_file_path, sheet_name="scores", nrows=20))
print("=================读scores表, 将student_id这一列作为索引列=======================")
print(pd.read_excel(exc_file_path, sheet_name=1, index_col="student_id"))
print("=================读scores表, 把分数变为150分制的分数=======================")
def func(x):
    return float(x) * 1.5
print(pd.read_excel(exc_file_path, sheet_name=1, converters={
    'math': func,
    'english': func,
    'physics': func
}))



#输出结果如下
=================指定sheet_name = scores 读scores表=======================
    student_id name  math  english  physics
0        20001   朱七    51       64       71
1        20002  冯思俊    63       83       62
2        20003  赵志宇   100       86       82
3        20004  秦八六    99       69       78
4        20005   王嘉    87       57       92
..         ...  ...   ...      ...      ...
95       20096   蒋欣    76       79       96
96       20097   郑浩    52       71       66
97       20098  赵豪思    60       50       64
98       20099  韩琪宇    91       68       88
99       20100  尤嘉俊    67       77       98

[100 rows x 5 columns]
=================读scores表的前20行=======================
    student_id name  math  english  physics
0        20001   朱七    51       64       71
1        20002  冯思俊    63       83       62
2        20003  赵志宇   100       86       82
3        20004  秦八六    99       69       78
4        20005   王嘉    87       57       92
5        20006  褚子欣    61       77       57
6        20007  蒋四十    88       96       56
7        20008   秦航    96       53       56
8        20009   陈四    66       80       50
9        20010  赵思佳    82       65       84
10       20011   赵伟    96       96       79
11       20012   吴涵    93       88       58
12       20013  陈一伟    81       79       60
13       20014   沈三   100       66       70
14       20015   尤二    60       94       90
15       20016  孙梓俊    91       69       67
16       20017   李杰    67       60       50
17       20018   吴十    52       95       93
18       20019  朱思思    61       90       59
19       20020  周宇三    80       55       94
=================读scores表, 将student_id这一列作为索引列=======================
           name  math  english  physics
student_id                             
20001        朱七    51       64       71
20002       冯思俊    63       83       62
20003       赵志宇   100       86       82
20004       秦八六    99       69       78
20005        王嘉    87       57       92
...         ...   ...      ...      ...
20096        蒋欣    76       79       96
20097        郑浩    52       71       66
20098       赵豪思    60       50       64
20099       韩琪宇    91       68       88
20100       尤嘉俊    67       77       98

[100 rows x 4 columns]
=================读scores表, 把分数变为150分制的分数=======================
    student_id name   math  english  physics
0        20001   朱七   76.5     96.0    106.5
1        20002  冯思俊   94.5    124.5     93.0
2        20003  赵志宇  150.0    129.0    123.0
3        20004  秦八六  148.5    103.5    117.0
4        20005   王嘉  130.5     85.5    138.0
..         ...  ...    ...      ...      ...
95       20096   蒋欣  114.0    118.5    144.0
96       20097   郑浩   78.0    106.5     99.0
97       20098  赵豪思   90.0     75.0     96.0
98       20099  韩琪宇  136.5    102.0    132.0
99       20100  尤嘉俊  100.5    115.5    147.0

[100 rows x 5 columns]

```





### DataFrame.to_excel

​	**将对象写入Excel的工作簿中**



| 参数： |
| ------ |

**①excel_writer：路径，文件 或 ExcelWriter 对象**

​	**文件路径或现有的ExcelWriter**

**②sheet_name：str，默认'sheet1'**

​	**要把DataFrame写入到哪个工作簿（sheet）**

**③columns：sequence 或 str列表，可选**

​	**要写入哪些列**

**④index_label：str 或 sequence，可选**

​	**指定索引列的列标签**

**⑤startrow: int,默认0**

​	**指定从第几行开始写入**

**⑥startcol: int，默认0**

​	**指定从第几列开始写入**



[详情参阅]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html





### # to_excel示例

```python
# 读取TOP250.xlsx的scores表，并计算每个科目的最高分，中位数和平均分，输出为Excel
exc_file_path = "./examples/TOP250.xlsx"
df = pd.read_excel(exc_file_path, sheet_name="scores")
print("========================读取出来的数据==============================")
print(df)
print("========================根据读取的数据计算出来新的DataFrame==============================")
df_3 = df[['math', 'english', 'physics']]
counts_df = df_3.apply(lambda col: pd.Series({"最高分": col.max(), "平均分": col.mean(), "中位数": col.quantile()}))
print(counts_df)
# 1、生成到新的xlsx中，命名为 scores_counts.xlsx
counts_df.to_excel("./examples/scores_counts.xlsx")

# 2、生成到原来的表中，名字自定
# engine="openpyxl"  openpyxl 追加时会保留已有单元格格式、公式、图表、筛选等；  其他引擎做不到。
with pd.ExcelWriter(exc_file_path, engine="openpyxl" mode='a') as writer:
    counts_df.to_excel(writer, sheet_name="统计")
print("执行成功")



#执行结果如下
========================读取出来的数据==============================
    student_id name  math  english  physics
0        20001   朱七    51       64       71
1        20002  冯思俊    63       83       62
2        20003  赵志宇   100       86       82
3        20004  秦八六    99       69       78
4        20005   王嘉    87       57       92
..         ...  ...   ...      ...      ...
95       20096   蒋欣    76       79       96
96       20097   郑浩    52       71       66
97       20098  赵豪思    60       50       64
98       20099  韩琪宇    91       68       88
99       20100  尤嘉俊    67       77       98

[100 rows x 5 columns]
========================根据读取的数据计算出来新的DataFrame==============================
       math  english  physics
最高分  100.00   100.00   100.00
平均分   75.37    76.78    72.96
中位数   76.50    79.50    72.00
执行成功
```





### **:warning:注意** ###

**:heavy_exclamation_mark:<span style='color: red; font-size: 19px'>这句话很危险</span>:heavy_exclamation_mark: ==counts_df.to_excel(exc_file_path, sheet_name="统计")==，这里exc_file_path 是源文件的路径，执行了这句代码后的结果是源文件里面只有新加的这个统计的工作簿，<span style='color: red; font-size: 19px'>原来的数据会丢失！！！</span>所以，如果想往Excel文件里写多个sheet，必须使用ExcelWriter写入，mode='a'进行追加sheet。**

<span style='color: blue;font-size:23px'>*所以，建议一定要先对原数据做备份，再进行写入操作*</span>





## 5、HTML

### #示例HTML

**[文件链接](G:\01作业\Pandas\0620文件读取练习), test.html**

![](G:\01资料\Pictures\read_html示例.png)







### pandas.read_html

​	**将HTML的table标签下的数据读取到DataFrame对象的列表中**



| 参数： |
| ------ |

**①io：str，path 对象 或 类文件对象**

​	**指定要读取的html，字符串可以是URL，类文件对象需实现`read()`方法**

**②flavor：{'lxml', 'html5lib', 'bs4'}或类列表，可选**

​	**指定解析引擎（或引擎列表），默认的None会尝试使用`lxml`进行解析，如果失败，则会使用`bs4 + html5lib`**

**③header: int 或 类列表，可选**

​	**指定要当作表头的行，如果是多级索引，则使用列表传入**

**④index_col：int 或 类列表，可选**

​	**要用作行索引的列**

**⑤skiprows: int, 类列表，可选**

​	**如果为int，则跳过前skiprows行，如果为列表，则跳过指定的某几行**

**⑥parse_dates：bool，可选**

​	**是否解析日期类型**

**⑦encoding：str，可选**

​	**用于解码HTML的编码集**

**⑧converters：字典，默认None**

​	**用于转换特定列中值的字典，键是列标签，值是callable（接受一个输入参数，即单元格的内容）**

**⑨na_values: iterable，默认None**

​	**指定被视为缺失值的values**

**⑩keep_default_na：bool，默认True**

​	**是否将默认的NA视为缺失值**



| 返回值： |
| -------- |

**:arrow_right:返回多个DataFrame的列表**





### **# 简单实例：** ###

```python
df_list = pd.read_html('test.html')			#读取的文件也可以是URL
for df in df_list:
    print(df)
    print("======================================")

    
#输出结果如下    
   员工ID  姓名   部门     职位        入职日期
0  1001  张三  技术部  前端工程师  2020-05-15
1  1002  李四  市场部   营销经理  2019-08-22
2  1003  王五  人事部   HR专员  2021-03-10
======================================
    部门  季度  预算(万元)  实际支出(万元)  差额(万元)
0  技术部  Q1    50.0      45.2     4.8
1  市场部  Q1    30.0      32.5    -2.5
2  人事部  Q1    20.0      18.3     1.7
3  技术部  Q2    55.0      52.1     2.9
4   总计  总计   155.0     148.1     6.9
======================================



#设置索引列，可以读取的时候设置，也可以读取出来使用DataFrame的set_index()方法设置
----------------------------------------------------------------------------------------------------
#html里有两个表，索引列必须设置为两个表里共有的列，这里都设置第一列为索引列
df_list = pd.read_html('test.html', index_col=0)		
print(df_list[0])
print("=" * 100)
print(df_list[1])


#输出结果如下，可以看到索引列都是第一列
            姓名   部门     职位        入职日期
employeeId                            
1001        张三  技术部  前端工程师  2020-05-15
1002        李四  市场部   营销经理  2019-08-22
1003        王五  人事部   HR专员  2021-03-10
===============================================================
               部门  季度  预算(万元)  实际支出(万元)  差额(万元)
departmentId                                   
2001          技术部  Q1    50.0      45.2     4.8
2002          市场部  Q1    30.0      32.5    -2.5
2003          人事部  Q1    20.0      18.3     1.7
2004          技术部  Q2    55.0      52.1     2.9



#skiprows参数
----------------------------------------------------------------------------------------------------
#1、skiprow = list
>>> pd.read_html('test.html', skiprows=[1, 2])				#跳过table数据的第1行和第2行，除表头
[   employeeId  姓名   部门    职位        入职日期
 0        1003  王五  人事部  HR专员  2021-03-10,
    departmentId   部门  季度  预算(万元)  实际支出(万元)  差额(万元)
 0          2003  人事部  Q1    20.0      18.3     1.7
 1          2004  技术部  Q2    55.0      52.1     2.9]


>>> pd.read_html('test.html', skiprows=[1])				#注意这个与下面的区别，这个是跳过第1行！！！
[   employeeId  姓名   部门    职位        入职日期
 0        1002  李四  市场部  营销经理  2019-08-22
 1        1003  王五  人事部  HR专员  2021-03-10,
    departmentId   部门  季度  预算(万元)  实际支出(万元)  差额(万元)
 0          2002  市场部  Q1    30.0      32.5    -2.5
 1          2003  人事部  Q1    20.0      18.3     1.7
 2          2004  技术部  Q2    55.0      52.1     2.9]



#2、skiprows = int
>>> pd.read_html('test.html', skiprows=1)				#跳过前1行！！！
[   1001  张三  技术部 前端工程师  2020-05-15
 0  1002  李四  市场部  营销经理  2019-08-22
 1  1003  王五  人事部  HR专员  2021-03-10,
    2001  技术部  Q1  50.0  45.2  +4.8
 0  2002  市场部  Q1  30.0  32.5  -2.5
 1  2003  人事部  Q1  20.0  18.3   1.7
 2  2004  技术部  Q2  55.0  52.1   2.9]



#converters参数
----------------------------------------------------------------------------------------------------
#应用：单位换算
def fun(x):
    return float(x) * 10000.0
pd.read_html('test.html', converters={
    '预算(万元)': fun,
    '实际支出(万元)': fun,
    '差额(万元)': fun
}, index_col=0)[1]

               部门  季度    预算(万元)  实际支出(万元)   差额(万元)
departmentId                                      
2001          技术部  Q1  500000.0  452000.0  48000.0
2002          市场部  Q1  300000.0  325000.0 -25000.0
2003          人事部  Q1  200000.0  183000.0  17000.0
2004          技术部  Q2  550000.0  521000.0  29000.0
```





## 6、SQL

### pandas.read_sql

**==pandas.read_sql(*sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None, dtype_backend=\<no_default>, dtype=None*)==**

​	**把SQL查询语句或数据库中的表解析成DataFrame**



| 参数： |
| ------ |

**①sql：str 或 SQLAlchemy Selectable(选择或文本对象)**

​	**要执行的SQL查询语句或表名**

**②con：ADBC Connection, SQLAlchemy connectable, str 或 sqlite3 connection**

​	**ADBC 提供了高性能的I/O，并支持原生类型。**

​	**使用SQLAlchemy 可以使用该库支持的任何数据库，SQLAlchemy支持几乎所有的主流关系型数据库**

​	**如果是DBAPI2对象，仅支持sqlite3**

**③index_col: str 或 str列表，可选，默认值None**

​	**要设置为索引的列**

**④coerce_float: bool，默认为True**

​	**尝试将非字符串、非数字对象的值转换为浮点数，这对SQL结果集很有用**

**⑤params：list，tuple或字典，可选，默认None**

​	**传递给执行方法的参数列表，传递参数的语法取决于数据库驱动程序**

**⑥parse_dates：列表或字典，默认None**

- **要解析为日期的列名列表**
- **`{column_name: format string}`或`{column_name: arg dict}`的字典，其中`arg dict`对应于`pandas.to_datetime()`的关键字参数，特别是对于没有本机Datetime支持的数据库非常有用**

**⑦dtype_backend: {'numpy_nullable', 'pyarrow'}，默认'numpy_nullable'**

**⑧dtype：类型名 或 列的字典**

​	**数据或者列的数据类型，例如`np.float64`或`{'a': np.float64, 'b': np.int32, 'c': str}`**



| 返回值： |
| -------- |

**:arrow_right:DataFrame或Iterator[DataFrame]**





### # SQL查询的执行顺序

1. **from和join：首先确定数据来源**
2. **where：对数据进行初步筛选**
3. **group by：对数据进行分组**
4. **having：对分组后的数据进行筛选**
5. **select：选择要返回的列**
6. **distinct：去除重复行**
7. **order by：对结果进行排序**
8. **limit/offset：限制返回的行数**





### # Python的sqlite3

**sqlite3——SQLite数据库的DB-API2.0接口**

​	**SQLite是一个C语言库，它可以提供一种轻量级的基于磁盘的数据库，这种数据库不需要独立的服务器进程，可以使用它来创建一个应用程序原型，然后再迁移到更大的数据库，比如Postgre 或 Oracle**



### :heavy_exclamation_mark: 一个实例

**基于磁盘的数据库建立：**

```python
# 导入Python的sqlite3库
import sqlite3

# 建立数据库连接
#调用 sqlite3.connect 函数来创建与当前工作目录下 steam.db 数据库的连接，如果不存在会创建此数据库
conn = sqlite3.connect("steam.db")
cur = conn.cursor()                 # 为了执行SQL语句并从SQL查询中取得结果，需要使用游标cursor


# 使用execute 函数可以执行一条SQL语句, 如果执行多条，请用executemany 函数
# 删除旧表
cur.execute("DROP TABLE IF EXISTS games")

# 创建表
cur.execute("""
CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    release_year INTEGER,
    price REAL,
    positive INTEGER,
    negative INTEGER
)
""")

# 插入数据
games = [
    ("GTA V", 2015, 29.99, 350000, 50000),
    ("The Witcher 3", 2015, 39.99, 450000, 30000),
    ("Stardew Valley", 2016, 14.99, 250000, 10000),
    ("Cyberpunk 2077", 2020, 59.99, 300000, 150000),
    ("CS:GO", 2012, 0.00, 600000, 100000),
]


cur.executemany("INSERT INTO games (name, release_year, price, positive, negative) VALUES (?, ?, ?, ?, ?)", games)
conn.commit()           #这里提交的原因是因为insert语句会隐式的创建一个事务，如果要将更改保存到数据库，则必须提交事务
```





#### **:a:连接对象是 sqlite3 connection** ####

**使用上述磁盘的数据库进行read_sql的操作**

```python
# 1. 从steam.db里的games表中选出价格30元以上的游戏的名字 和 发布年份，并转成DataFrame
sql_query = """
select name, release_year
from games
where price > 30 """
pd.read_sql(sql_query, conn)

             name  release_year
0   The Witcher 3          2015
1  Cyberpunk 2077          2020


# 2. 从steam.db里获取完整的games表，得出相应的DataFrame
query_all = """
select *
from games"""

# 把games表的id列作为行索引
df_index_id = pd.read_sql(query_all, conn, index_col=['id'])
print(df_index_id)

              name  release_year  price  positive  negative
id                                                         
1            GTA V          2015  29.99    350000     50000
2    The Witcher 3          2015  39.99    450000     30000
3   Stardew Valley          2016  14.99    250000     10000
4   Cyberpunk 2077          2020  59.99    300000    150000
5            CS:GO          2012   0.00    600000    100000



#3、查询评分最高的三个游戏
query = """
SELECT name, price, positive, negative,
       ROUND(1.0 * positive / (positive + negative), 3) AS rating
FROM games
ORDER BY rating DESC
LIMIT 3
"""

>>> for row in cur.execute(query):					#可以迭代
    print(row)
('Stardew Valley', 14.99, 250000, 10000, 0.962)
('The Witcher 3', 39.99, 450000, 30000, 0.938)
('GTA V', 29.99, 350000, 50000, 0.875)


>>> pd.read_sql(query, conn)						
             name  price  positive  negative  rating
0  Stardew Valley  14.99    250000     10000   0.962
1   The Witcher 3  39.99    450000     30000   0.938
2           GTA V  29.99    350000     50000   0.875
```



**:warning:最后一定要关闭连接，避免内存占用**

```python
conn.close()
```





#### :b:**连接对象是SQLAlchemy connectable**

​	**SQLAlchemy 是Python的SQL工具集，支持几乎所有主流关系型数据库，通过SQLAlchemy中间层，可以和多种数据库连接。**

​	**其中，SQLAlchemy 的 Engine 是与数据库交互的核心接口，负责管理数据库连接池和执行SQL操作，使用`sqla.create_engine()`可创建引擎，其常见的参数有：**

- **SQLite**: `sqlite:///relative/path.db` 或 `sqlite:////absolute/path.db`
- **PostgreSQL**: `postgresql+psycopg2://user:pass@host:port/dbname`
- **MySQL**: `mysql+pymysql://user:pass@host:port/dbname`
- **Oracle**: `oracle+cx_oracle://user:pass@host:port/dbname`
- **SQL Server**: `mssql+pyodbc://user:pass@host:port/dbname?driver=ODBC+Driver+17+for+SQL+Server`



**使用上面创建的steam.db数据库**

```python
import sqlalchemy as sqla

engine = sqla.create_engine('sqlite:///steam.db')
conn = engine.connect()
>>> pd.read_sql("SELECT * FROM games", conn)
   id            name  release_year  price  positive  negative
0   1           GTA V          2015  29.99    350000     50000
1   2   The Witcher 3          2015  39.99    450000     30000
2   3  Stardew Valley          2016  14.99    250000     10000
3   4  Cyberpunk 2077          2020  59.99    300000    150000
4   5           CS:GO          2012   0.00    600000    100000


>>> pd.read_sql("SELECT * FROM games", conn, index_col="id")
              name  release_year  price  positive  negative
id                                                         
1            GTA V          2015  29.99    350000     50000
2    The Witcher 3          2015  39.99    450000     30000
3   Stardew Valley          2016  14.99    250000     10000
4   Cyberpunk 2077          2020  59.99    300000    150000
5            CS:GO          2012   0.00    600000    100000
```



**:warning:最后一定要关闭连接，避免内存占用**

```python
conn.close()
```





# 五、Pandas扩展数据类型

​		**在大多数情况下，Pandas使用NumPy数组和数据类型来表示Series或DataFrame的各个列，NumPy支持`float`, `int`, `bool`, `timedelta64[ns]`和`datetime64[ns]`，注意，NumPy不支持时区感知的日期时间。**

​		**对于Pandas来说，无论平台是什么（32位还是64位），默认情况下，整数类型为`int64`，浮点数类型为`float64`**

​		**而对于NumPy来说，NumPy在创建数组时会选择与平台相关的类型，所以在32位的平台上，NumPy数组默认`int32`**



**下面是Pandas的扩展数据类型**

|      数据类型      |    标量     |                   Array                    |                            String                            |
| :----------------: | :---------: | :----------------------------------------: | :----------------------------------------------------------: |
| `DatetimeTZDtype`  | `Timestamp` |           `arrays.DatetimeArray`           |                    `datetime64[ns, <tz>]`                    |
| `CategoricalDtype` |   `none`    |               `Categorical`                |                          `category`                          |
|   `PeriodDtype`    |  `Period`   | `arrays.PeriodArray`<br />`Period[<freq>]` |                       `period[<freq>]`                       |
|   `SparseDtype`    |   `none`    |            `arrays.SparseArray`            |            `Sparse`,`Sparse[int]`,`Sparse[float]`            |
|  `IntervalDtype`   | `Interval`  |           `arrays.IntervalArray`           | `interval`,`Interval`,<br />`Interval[<numpy_dtype>]`<br />`Interval[datetime64[ns, <tz>]]`<br />`Interval[timedelta64[<freq>]]` |
|  `Inte64Dtype`...  |   `none`    |           `arrays.IntegerArray`            | `Int8`,`Int16`,`Int32`,`Int64`<br />`UInt8`,`UInt16`,`UInt32`,`UInt64` |
| `Float64Dtype`...  |   `none`    |           `arrays.FloatingArray`           |                     `Float32`,`Float64`                      |
|   `StringDtype`    |    `str`    |            `arrays.StringArray`            |                           `string`                           |
|   `BooleanDtype`   |   `bool`    |           `arrays.BooleanArray`            |                          `boolean`                           |

**Pandas有两种存储字符串的方式：**

- **`object`dtype，可以保存任何Python对象，包括字符串**
- **`StringDtype`，专用于字符串**





**DataFrame可以通过调用`DataFrame.dtypes.value_counts()`来找到每种类型的列数**

```python
dft = pd.DataFrame(
    {
        "A": np.random.rand(3),
        "B": 1,
        "C": "foo",
        "D": pd.Timestamp("20010102"),
        "E": pd.Series([1.0] * 3).astype("float32"),
        "F": False,
        "G": pd.Series([1] * 3, dtype="int8"),
    }
)
>>> print(dft.dtypes.value_counts())
float64          1
int64            1
object           1
datetime64[s]    1
float32          1
bool             1
int8             1
Name: count, dtype: int64

```





**在数据类型不兼容的情况下，一般会向上转换以便适合所有数据。你也可以使用`astype()`自定义数据类型转换**

## Series/DataFrame.astype

**==Series/DataFrame.astype(*dtype, copy=None, errors='raise'*)==**

​	**将pandas对象转换为指定的dtype**



| 参数： |
| ------ |

**①dtype：str,数据类型，Series 或 colname -> dtype的映射**

​	**可用的dtype有str，numpy.dtype，pandas.ExtensionDtype或Python类型**

**②copy：bool，默认为True**

​	**`copy = True`时返回副本，指定`copy = False`时要非常小心，会导致数据丢失等情况**

**③errors: {'raise', 'ignore'}，默认'raise'**

​	**当异常出现要做什么，`raise`表示抛出异常，`ignore`表示忽略异常并返回原数据**



```python
>>> d = {'col1': [1, 2], 'col2': [3, 4]}
>>> df = pd.DataFrame(data=d)
>>> df.dtypes				#默认int64
col1    int64
col2    int64
dtype: object


#全部转换为int32
>>> df.astype('int32').dtypes
col1    int32
col2    int32
dtype: object


#只把col1的数据类型转换为int32
>>> df.astype({'col1': 'int32'}).dtypes
col1    int32
col2    int64
dtype: object


#指定数据类型创建
>>> ser = pd.Series([1, 2], dtype='int32')
>>> ser
0    1
1    2
dtype: int32
>>> ser.astype('int64')
0    1
1    2
dtype: int64


#将Series转换为分类类型，无序
>>> ser.astype('category')
0    1
1    2
dtype: category
Categories (2, int32): [1, 2]


#将Series转成自定义的有序分类类型
>>> from pandas.api.types import CategoricalDtype
>>> cat_dtype = CategoricalDtype(
...     categories=[2, 1], ordered=True)
>>> ser.astype(cat_dtype)
0    1
1    2
dtype: category
Categories (2, int64): [2 < 1]


#datetime类型
>>> ser_date = pd.Series(pd.date_range('20200101', periods=3))
>>> ser_date
0   2020-01-01
1   2020-01-02
2   2020-01-03
dtype: datetime64[ns]
```





**对于一维数据，`to_numeric()`可以转换为数字数据类型，`to_datetime()`可以转换为日期时间对象，`to_timedelta()`可以转换为timedelta对象，对于二维的DataFrame，可以使用`apply()`对每一列进行数据类型转换**

```python
In [407]: import datetime

In [408]: df = pd.DataFrame([["2016-07-09", datetime.datetime(2016, 3, 2)]] * 2, dtype="O")

In [409]: df
Out[409]: 
            0                    1
0  2016-07-09  2016-03-02 00:00:00
1  2016-07-09  2016-03-02 00:00:00

In [410]: df.apply(pd.to_datetime)
Out[410]: 
           0          1
0 2016-07-09 2016-03-02
1 2016-07-09 2016-03-02

In [411]: df = pd.DataFrame([["1.1", 2, 3]] * 2, dtype="O")

In [412]: df
Out[412]: 
     0  1  2
0  1.1  2  3
1  1.1  2  3

In [413]: df.apply(pd.to_numeric)
Out[413]: 
     0  1  2
0  1.1  2  3
1  1.1  2  3

In [414]: df = pd.DataFrame([["5us", pd.Timedelta("1day")]] * 2, dtype="O")

In [415]: df
Out[415]: 
     0                1
0  5us  1 days 00:00:00
1  5us  1 days 00:00:00

In [416]: df.apply(pd.to_timedelta)
Out[416]: 
                       0      1
0 0 days 00:00:00.000005 1 days
1 0 days 00:00:00.000005 1 days
```



## # NumPy数据类型树

**所有的NumPy dtype 都是`numpy.generic`的子类**

```python
#返回NumPy的数据类型树
def subdtypes(dtype):
    subs = dtype.__subclasses__()
    if not subs:
        return dtype
    return [dtype, [subdtypes(dt) for dt in subs]]

>>> subdtypes(np.generic)

[numpy.generic,
 [[numpy.number,
   [[numpy.integer,
     [[numpy.signedinteger,
       [numpy.int8,
        numpy.int16,
        numpy.intc,
        numpy.int32,
        numpy.int64,
        numpy.timedelta64]],
      [numpy.unsignedinteger,
       [numpy.uint8, numpy.uint16, numpy.uintc, numpy.uint32, numpy.uint64]]]],
    [numpy.inexact,
     [[numpy.floating,
       [numpy.float16, numpy.float32, numpy.float64, numpy.longdouble]],
      [numpy.complexfloating,
       [numpy.complex64, numpy.complex128, numpy.clongdouble]]]]]],
  [numpy.flexible,
   [[numpy.character, [numpy.bytes_, numpy.str_]],
    [numpy.void, [numpy.record]]]],
  numpy.bool_,
  numpy.datetime64,
  numpy.object_]]
```



**其中intc和uintc表示与C语言兼容**



```mermaid
graph LR
    A[numpy.generic] --> B[numpy.number]
    B --> B1[numpy.integer]
    B1 --> B11[numpy.signedinteger]
    B11 --> B111["numpy.int8, int16, intc, int32, int64, timedelta64"]
    B1 --> B12[numpy.unsignedinteger]
    B12 --> B121["numpy.uint8, uint16, uintc, uint32, uint64"]

    B --> B2[numpy.inexact]
    B2 --> B21[numpy.floating]
    B21 --> B211["numpy.float16, float32, float64, longdouble"]
    B2 --> B22[numpy.complexfloating]
    B22 --> B221["numpy.complex64, complex128, clongdouble"]

    A --> C[numpy.flexible]
    C --> C1[numpy.character]
    C1 --> C11["numpy.bytes_, str_"]
    C --> C2[numpy.void]
    C2 --> C21["numpy.record"]

    A --> D[numpy.bool_]
    A --> E[numpy.datetime64]
    A --> F[numpy.object_]
```





# 六、Categorical Data

​		**`Categoricals`是Pandas的数据类型，对应于统计学中的分类变量（数量有限且通常固定），例如：性别、社会阶层、血型和观察时间等，其类别可以有序也可以无序，对于观测时间必须有序，而对于血型来讲顺序就不那么重要了。**

**分类数据类型在以下情况下很有用：**

- **仅由几个不同值组成的字符串变量。将这样的字符串变量转换为分类变量可以节省一些内存，如：**

```python
ser = pd.Series(['foo', 'bar', 'baz'] * 1000)
>>> ser.memory_usage()
24132

>>> ser.astype("category").memory_usage()
3264
```

- **变量的词汇顺序与逻辑顺序（"一"，"二"，"三"）不同，通过转换成分类变量并指定类别的顺序，排序和最大/最小操作将使用逻辑顺序而不是词汇顺序，如：**

```python
s = pd.Series(pd.Categorical(["a", "b", "c", "a"], ordered=True))
>>> s.sort_values()
0    a
3    a
1    b
2    c
dtype: category
Categories (3, object): ['a' < 'b' < 'c']

>>> s.min(), s.max()
('a', 'c')
```

- **应该被当成分类变量的其他情况**



## 1、CategoricalDtype

### （1）构造方法

**==pandas.CategoricalDType(*categories=None, ordered=False*)==**

​	**具有类别和顺序的可分类数据的数据类型**



| 参数： |
| ------ |

**①categories：序列，可选**

​	**必须唯一，且不允许包含任何空值。**

**②ordered：bool或None，默认为False**

​	**此分类是否被视为有序分类**



**所有的`CategoricalDtype`实例都等于字符串`category`**

```python
c1 = CategoricalDtype(["a", "b", "c"], ordered=False)
>>> c1 == "category"
True
```





### （2）属性

**仅有两个属性**

|    属性值    |           说明            |
| :----------: | :-----------------------: |
| `categories` | 包含`Index`允许的唯一类别 |
|  `ordered`   | 类别之间是否具有有序关系  |



```python
t = pd.CategoricalDtype(categories=['b', 'a'], ordered=True)
ser = pd.Series(['a', 'b', 'c', 'a'], dtype=t)
print("==============原Series================")
print(ser)
print("==============分类类型的categories================")
print(t.categories)
print("==============分类类型的ordered================")
print(t.ordered)


#输出结果如下
==============原Series================
0      a
1      b
2    NaN
3      a
dtype: category
Categories (2, object): ['b' < 'a']
==============分类类型的categories================
Index(['b', 'a'], dtype='object')
==============分类类型的ordered================
True
```





## 2、Categorical

### （1）构造方法

**==pandas.Categorical(*values, categories=None, ordered=None, dtype=None, fastpath=\<no_default>, copy=True*)==**

​	**分类变量的风格是经典的R语言风格。**

​	**分类变量只能采用有限且通常固定数量的可能值（类别），它可能有序，但无法进行数值运算。**

​	**Categorical的所有值要么在categories中，要么在np.nan中，分配类别之外的值将引发[ValueError][]，顺序由categories的顺序定义**



| 参数： |
| ------ |

**①values：列表**

​	**分类的值，如果指定了类别，则不在类别中的值会被替换成NaN**

**②categories：Index（唯一）， 可选**

​	**此分类的唯一类别，如果未指定此参数，则类别是values的唯一值列表，如果指定了有序，则按在values中出现的顺序排序**

**③ordered：bool，默认False**

​	**指定此分类是否有序**

**④dtype：CategoricalDType**

​	**分类数据类型**



### （2）属性



|    属性名    |             说明             |
| :----------: | :--------------------------: |
| `categories` |          分类的类别          |
|   `codes`    | 该分类索引的类别代码，不可写 |
|  `ordered`   |       类别之间是否有序       |
|   `dtype`    |         分类数据类型         |



### （3）类方法

|    方法名    |                             说明                             |
| :----------: | :----------------------------------------------------------: |
| `from_codes` |      根据code(分类编码)和categories或dtype创建分类类型       |
| `__array__`  | NumPy的数组接口，需要使用`numpy.array()`和`numpy.asarray()`调用 |



**分类编码为[0, 1, 0, 1]，分类为['a', 'b']，则可以通过他们来创建Categorical对象，使用`pandas.Categorical.from_codes()`**

```python
>>> dtype = pd.CategoricalDtype(['a', 'b'], ordered=True)
>>> pd.Categorical.from_codes(codes=[0, 1, 0, 1], dtype=dtype)
['a', 'b', 'a', 'b']
Categories (2, object): ['a' < 'b']
```





```python
c = pd.Categorical(['a', 'b', 'c', 'a', 'd', 'b', 'c', 'd'])
print("================不指定categories参数=======================")
print(c)
print("================指定 categories=['c', 'b', 'a']=======================")
c = pd.Categorical(['a', 'b', 'c', 'a', 'd', 'b', 'c', 'd'], categories=['c', 'b', 'a'])
print(c)
print("================指定 categories=['a', 'b', 'c', 'd'], ordered = true=======================")
c = pd.Categorical(['a', 'b', 'c', 'a', 'd', 'b', 'c', 'd'], categories=['a', 'b', 'c', 'd'], ordered=True)
print(c)
print("================该分类对象分类的类别=======================")
print(c.categories)
print("================分类的编码，表示values中每个元素对应的分类的编码=======================")
print(c.codes)
print("================该分类对象是否有序=======================")
print(c.ordered)
print("================该分类对象的数据类型=======================")
print(c.dtype)
print("================该分类对象的最大/最小分类=======================")
print(c.min(), c.max())


#输出结果如下
================不指定categories参数=======================
['a', 'b', 'c', 'a', 'd', 'b', 'c', 'd']
Categories (4, object): ['a', 'b', 'c', 'd']
================指定 categories=['c', 'b', 'a']=======================
['a', 'b', 'c', 'a', NaN, 'b', 'c', NaN]
Categories (3, object): ['c', 'b', 'a']
================指定 categories=['a', 'b', 'c', 'd'], ordered = true=======================
['a', 'b', 'c', 'a', 'd', 'b', 'c', 'd']
Categories (4, object): ['a' < 'b' < 'c' < 'd']
================该分类对象分类的类别=======================
Index(['a', 'b', 'c', 'd'], dtype='object')
================分类的编码，表示values中每个元素对应的分类的编码=======================
[0 1 2 0 3 1 2 3]
================该分类对象是否有序=======================
True
================该分类对象的数据类型=======================
category
================该分类对象的最大/最小分类=======================
a d
```



```python
>>> cat = pd.Categorical(['a', 'b'], ordered=True)
>>> cat
['a', 'b']
Categories (2, object): ['a' < 'b']
>>> cat.dtype
CategoricalDtype(categories=['a', 'b'], ordered=True, categories_dtype=object)
```





## 3、对象创建

### （1）Series创建

:a:**在构造Series时指定`dtype=category`，推断分类的类型**

```python
In [1]: s = pd.Series(["a", "b", "c", "a"], dtype="category")

In [2]: s
Out[2]: 
0    a
1    b
2    c
3    a
dtype: category
Categories (3, object): ['a', 'b', 'c']
```



**通过`pandas.Categorical`对象传递给Series或DataFrame的某一列**

```python
cat = pd.Categorical(['a', 'b', 'c', 'a'], categories=['a', 'b', 'c'], ordered=True)
ser = pd.Series(cat)
print("=================使用Categorical创建Series===============")
print(ser)
print("=================使用Categorical创建DataFrame===============")
df = pd.DataFrame({'A': ['a', 'd', 'e', 'g'], 'B': cat})
print(df)
print(df.dtypes)


#输出结果如下
=================使用Categorical创建Series===============
0    a
1    b
2    c
3    a
dtype: category
Categories (3, object): ['a' < 'b' < 'c']
=================使用Categorical创建DataFrame===============
   A  B
0  a  a
1  d  b
2  e  c
3  g  a
A      object
B    category
dtype: object
```



**:b:通过`Series.astype(CategoricalDType)`来创建Series，指定具体的分类类型**

```python
In [26]: from pandas.api.types import CategoricalDtype

In [27]: s = pd.Series(["a", "b", "c", "a"])

In [28]: cat_type = CategoricalDtype(categories=["b", "c", "d"], ordered=True)

In [29]: s_cat = s.astype(cat_type)

In [30]: s_cat
Out[30]: 
0    NaN
1      b
2      c
3    NaN
dtype: category
Categories (3, object): ['b' < 'c' < 'd']
```





### （2）DataFrame创建

:a:**通过传递`dtype=category`的方式构造DataFrame**

```python
df = pd.DataFrame({'A': list('apple'), 'B': list('abade')}, dtype='category')
print("==============DataFrame======================")
print(df)
print("================DataFrame每列的数据类型====================")
print(df.dtypes)
print("==============虽然两列的数据类型都为category，但它们的分类类别是不同的======================")
print("==============DataFrame的A列======================")
print(df['A'])
print("==============DataFrame的B列======================")
print(df['B'])


#输出结果如下
==============DataFrame======================
   A  B
0  a  a
1  p  b
2  p  a
3  l  d
4  e  e
================DataFrame每列的数据类型====================
A    category
B    category
dtype: object
==============虽然两列的数据类型都为category，但它们的分类类别是不同的======================
==============DataFrame的A列======================
0    a
1    p
2    p
3    l
4    e
Name: A, dtype: category
Categories (4, object): ['a', 'e', 'l', 'p']
==============DataFrame的B列======================
0    a
1    b
2    a
3    d
4    e
Name: B, dtype: category
Categories (4, object): ['a', 'b', 'd', 'e']
```



**:b:通过`DataFrame.astype(CategoricalDType)`来创建DataFrame，指定具体的分类类型**

```python
In [31]: from pandas.api.types import CategoricalDtype

In [32]: df = pd.DataFrame({"A": list("abca"), "B": list("bccd")})

In [33]: cat_type = CategoricalDtype(categories=list("abcd"), ordered=True)

In [34]: df_cat = df.astype(cat_type)

In [35]: df_cat["A"]
Out[35]: 
0    a
1    b
2    c
3    a
Name: A, dtype: category
Categories (4, object): ['a' < 'b' < 'c' < 'd']

In [36]: df_cat["B"]
Out[36]: 
0    b
1    c
2    c
3    d
Name: B, dtype: category
Categories (4, object): ['a' < 'b' < 'c' < 'd']
```





## 4、排序

**使用`as_ordered()`和`as_unordered()`将分类对象设置为有序或无序，默认情况下，这将返回一个新对象**

```python
s = pd.Series(pd.Categorical(["a", "b", "c", "a"], ordered=False))
print(s.cat.as_ordered())
print(s.cat.as_unordered())

0    a
1    b
2    c
3    a
dtype: category
Categories (3, object): ['a' < 'b' < 'c']
0    a
1    b
2    c
3    a
dtype: category
Categories (3, object): ['a', 'b', 'c']
```



## 5、内存使用

**一般情况下，`Categorical`数据类型表示的数据具有<span style='color: red;font-size: 19px'>更小</span>的内存空间**

**`Categorical`数据类型的内存占用与类别数量和数据长度成正比，而`object`数据类型则是一个常数乘以数据长度**

```python
In [242]: s = pd.Series(["foo", "bar"] * 1000)

# object dtype
In [243]: s.nbytes
Out[243]: 16000

# category dtype
In [244]: s.astype("category").nbytes
Out[244]: 2016
```



<span style='color: red'>**但是,如果类别的数量接近数据的长度**</span>，**`Categorical`则将使用更多的内存来表示相应的数据，甚至比`object`表示此数据占用的内存多**

```python
In [245]: s = pd.Series(["foo%04d" % i for i in range(2000)])

# object dtype
In [246]: s.nbytes
Out[246]: 16000

# category dtype
In [247]: s.astype("category").nbytes
Out[247]: 20000
```



# 七、Groupby：split-apply-combine

**我们所说的“分组”是指涉及以下一个或多个步骤的过程：**

- 根据某些标准将数据**分成几组**
- 对每个组独立的**应用**一个函数
- 将结果**组合**成数据结构



**其中，拆分步骤最直接；在应用步骤中，我们可能希望执行以下操作之一：**

- **聚合：**计算每个组的一个或多个汇总统计数据，例如计算总和、平均值，或者计算组的大小或数量等
- **转换：**执行特定组的计算并返回一个索引话的对象，例如标准化组内的数据，填充组内的缺失值等
- **过滤：**根据分组计算结果True和False，丢弃一些组，例如丢弃属于少数成员组的数据，根据组的总和或平均值过滤组等

**这一类的许多操作都是在GroupBy对象上定义的**



## 1、分组（`GroupBy`）

**一般情况下，我们将分组统称为键，分组的抽象定义是提供标签到组名的映射，映射可以通过多种不同的方式指定：**

- **一个Python函数，在每个索引标签上调用**
- **与索引长度相同的列表或NumPy数组**
- **字典或Series，提供`label -> group name`的映射**
- **对于DataFrame对象，表示用于分组的列名或索引级别名称的字符串**



**`df.groupby(pd.Grouper(key="Animal"))`等价于`df.groupby('Animal')`**



### DataFrame.groupby

**==DataFrame.groupby(*by=None, axis=\<no_default>, level=None, as_index=True, sort=False, group_keys=True, observed=True, dropna=True*)==**

​	**使用mapper或列的Series对DataFrame进行分组**



| 参数： |
| ------ |

**①by：mapping，function，label，pd.Grouper 并且 Grouper的列表**

​	**用于确定分组**

- **如果by是函数，则会被对象索引的每个值调用**
- **如果是字典或Series，则字典或Series的value将被用作分组依据**
- **如果是一个列表或ndarray，则根据所传的值来确定分组**

**②axis：{0 or ‘index’, 1 or ‘columns’}, 默认 0**

​	**沿哪个轴分组，对于`axis=1`的情况，可以使用`df.T.groupby()`进行分组**

**③level：int，层级名，或者层级的序列，默认None**

​	**指定对哪个层级分组**

**④as_index：bool，默认True**

​	**把组标签当作索引返回，仅与DataFrame输入相关，`as_index=False`是SQL风格的分组输出**

**⑤sort：bool，默认False**

​	**是否对组键进行排序**

**⑥group_keys：bool， 默认True**

​	**当调用apply且`by`参数生成一个类索引的结果时，将组键添加到索引中以标识各个部分，默认情况下，当结果的索引（和列）标签与输入匹配时，不包含组键，否则包含组键**

**⑦observed：bool，默认True**

​	**如果某一个分组是分类对象时，此参数有用。如果为True，仅仅显示分类对象组的数据，否则，会展示所有分组数据**

**⑧dropna：bool，默认True**

​	**如果为True并且组键中包含缺失值，缺失值所在的行的数据会被删除，如果为False，NA值也会被当作分组的键**



| 返回值： |
| -------- |

**:arrow_right:返回pandas.api.typing.DataFrameGroupBy分组对象，其中包含分组信息**





**对于如下的DataFrame**

```python
df = pd.DataFrame(
       {
           "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
           "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
           "C": np.random.randn(8),
           "D": np.random.randn(8),
       }
   )

>>> df
     A      B         C         D
0  foo    one -1.286131 -0.734406
1  bar    one  0.529669  0.862804
2  foo    two  0.423158 -0.958339
3  bar  three -0.527956 -0.003053
4  foo    two -0.224038  0.332587
5  bar    two  0.591006  0.084048
6  foo    one  0.632210 -0.330921
7  foo  three -0.339519  0.710331
```



*注意！`df.groupby('A')` 只是  `df.groupby(df['A'])` 的语法糖*

```python
In [7]: grouped = df.groupby("A")

In [8]: grouped = df.groupby("B")

In [9]: grouped = df.groupby(["A", "B"])
```



**如果将A和B列设置为多级索引，我们可以分组除了B之外的所有列，实现如下：**

```python
df1 = df.set_index(['A', 'B'])
print(df1.groupby(level=df1.index.names.difference(['B'])).sum())


			C         D
A                      
bar -0.976104  0.315275
foo -1.785249 -2.488482
```



**注意，<span style='color: red; font-size: 19px'>直到需要的时候分组才会进行</span>，成功的创建GroupBy对象仅仅是验证了传递了一个有效的映射**



### （1）GroupBy 排序和缺失值

**`sort`和`dropna`参数控制GroupBy的排序和缺失值处理的行为**

**有一点需要说明的是，`sort=False`会提高程序的性能**

```python
df = pd.DataFrame({"X": ["B", "B", "A", "A", "C", "C"], "Y": [1, 2, 3, 4, 5, 6], "Z": np.arange(10, 4, -1)})
print("===============原DataFrame=====================")
print(df)


===============原DataFrame=====================
   X  Y   Z
0  B  1  10
1  B  2   9
2  A  3   8
3  A  4   7
4  C  5   6
5  C  6   5



# groupby的排序，默认已排序，sort=False表示按原DataFrame的顺序，排序选项默认值官方文档后续可能会改
==================df.groupby('X').sum()========================
    Y   Z
X        
A   7  15
B   3  19
C  11  11
==================df.groupby('X', sort=False).sum()========================
    Y   Z
X        
B   3  19
A   7  15
C  11  11



# 缺失值处理，是否把缺失值纳入分组键中
==================设置缺失值 df.iloc[2, 0] = np.nan ========================
==================df.groupby('X').sum()========================
    Y   Z
X        
A   4   7
B   3  19
C  11  11
==================df.groupby('X', dropna=False).sum()========================
      Y   Z
X          
A     4   7
B     3  19
C    11  11
NaN   3   8
```





### （2）GroupBy对象的属性

**GroupBy的属性和常用方法**

|             属性或方法              |                  描述                  |
| :---------------------------------: | :------------------------------------: |
|              `groups`               |   返回分组的字典（ 组名-> 索引列表）   |
|              `ngroups`              |                分组数量                |
|              `indices`              | 类似groups，但返回整数索引而非索引标签 |
|              `size()`               |             返回每组的行数             |
|          `get_group(name)`          |            获取某个组的数据            |
| `max()/min()/std()/var()/cumprod()` |             大部分统计方法             |





```python
df = pd.DataFrame({"X": ["B", "B", "A", "A", "C", "C"], "Y": [1, 2, 3, 4, 5, 6], "Z": np.arange(10, 4, -1)}, index=list('abcdef'))
print("===============原DataFrame=====================")
print(df)
gb_x = df.groupby('X')
print("===============gb_x.groups 返回分组的字典 分类名-》索引名===================")
print(gb_x.groups)
print("===============gb_x.ngroups===================")
print(gb_x.ngroups)
print("===============gb_x.indices 返回分组的字典 分类名-》整数索引数组===================")
print(gb_x.indices)
print("===============返回每组多少个元素===================")
print(gb_x.size())
print("===============获取B组的数据===================")
print(gb_x.get_group('B'))




# 输出结果如下
===============原DataFrame=====================
   X  Y   Z
a  B  1  10
b  B  2   9
c  A  3   8
d  A  4   7
e  C  5   6
f  C  6   5
===============gb_x.groups 返回分组的字典 分类名-》索引名===================
{'A': ['c', 'd'], 'B': ['a', 'b'], 'C': ['e', 'f']}
===============gb_x.ngroups===================
3
===============gb_x.indices 返回分组的字典 分类名-》整数索引数组===================
{'A': array([2, 3], dtype=int64), 'B': array([0, 1], dtype=int64), 'C': array([4, 5], dtype=int64)}
===============返回每组多少个元素===================
X
A    2
B    2
C    2
dtype: int64
===============获取B组的数据===================
   X  Y   Z
a  B  1  10
b  B  2   9
```



### （3）多级索引的GroupBy

**对于如下的DataFrame**

```python
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["doo", "doo", "bee", "bee", "bop", "bop", "bop", "bop"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
index = pd.MultiIndex.from_arrays(arrays, names=["first", "second", "third"])
df = pd.DataFrame({'A':np.arange(8), 'B':np.arange(10, 2, -1)}, index=index)
print(df)


                    A   B
first second third       
bar   doo    one    0  10
             two    1   9
baz   bee    one    2   8
             two    3   7
foo   bop    one    4   6
             two    5   5
qux   bop    one    6   4
             two    7   3
```



```python
===============df.groupby(level=2).sum()====================
        A   B
third        
one    12  28
two    16  24
===============df.groupby(level='first').sum()====================
        A   B
first        
bar     1  19
baz     5  15
foo     9  11
qux    13   7
===============df.groupby(level=['first', 'second']).sum()====================
               A   B
first second        
bar   doo      1  19
baz   bee      5  15
foo   bop      9  11
qux   bop     13   7
===============df.groupby(["second A"]).sum()====================
           B
second A    
bee    2   8
       3   7
bop    4   6
       5   5
       6   4
       7   3
doo    0  10
       1   9
```



### （4）GroupBy对象可迭代

```python
#基于此DataFrame
					A   B
first second third       
bar   doo    one    0  10
             two    1   9
baz   bee    one    2   8
             two    3   7
foo   bop    one    4   6
             two    5   5
qux   bop    one    6   4
             two    7   3
    
    
    
for name, group in df.groupby(level='third'):
    print(name)
    print(group)
  

#输出结果如下
#第一组
===============================
one								
                    A   B		
first second third       
bar   doo    one    0  10
baz   bee    one    2   8
foo   bop    one    4   6
qux   bop    one    6   4

#第二组
===============================
two
                    A  B
first second third      
bar   doo    two    1  9
baz   bee    two    3  7
foo   bop    two    5  5
qux   bop    two    7  3
```







## 2、聚合（`Aggregation`）

### Ser/dfGroupBy.agg/aggregation

**==SeriesGroupBy/DataFrameGroupBy.agg/aggregation(*func, \*args, engine=None, engine_kwargs=None, \*\*kwargs*)==**

​	**在特定的轴上使用一种或多种操作对分组元素进行聚合**



| 参数： |
| ------ |

**①func：function，str，list，dict或None**

​	**聚合数据所使用的函数。如果是一个函数，则必须在传递DataFrame或传递给DataFrame.apply时起作用**

​	**可接受的组合有：**

- **匿名函数**
- **自定义函数名称**
- **函数名或函数的列表，例如`[np.sum, 'mean']`**
- **字典，轴标签 -> 函数、函数名或或函数列表**
- **None，在这种情况下，Named Aggregation使用`**kwargs`参数**

**②\*args**

​	**要传递给func的位置参数**

**③engine：str，默认None**

​	**可选的有`cython`，`numba`，`None`**

**④engine_kwargs：dict，默认None**



| 返回值： |
| -------- |

**:arrow_right:Series或DataFrame**





### （1）内置的聚合方法

**许多常见的函数都内置与GroupBy对象中，以方便使用**

|       方法名        |               描述                |
| :-----------------: | :-------------------------------: |
|       `any()`       |    判断组内的某一个值是否为真     |
|       `all()`       |     判断组内的所有值是否为真      |
|      `count()`      |     计算组内的非缺失值的数量      |
|    `max()/min()`    |      计算每个组的最大/最小值      |
|  `first()/last()`   | 显示每个组出现的第一个/最后一个值 |
| `idxmax()/idxmin()` |    计算每个组最大/最小值的下标    |
|      `mean()`       |         计算每组的平均值          |
|       `sum()`       |          对组内元素求和           |
|     `median()`      |        计算每个组的中位数         |
|    `quantile()`     |        计算每个组的分位数         |
|    `std()/var()`    |      计算每个组的标准差/方差      |
|      `prod()`       |      计算组内元素的累积乘积       |
|     `nunique()`     |       计算组内有几个唯一值        |



### （2）自定义函数

**对于如下的DataFrame**

```python
df = pd.DataFrame({"X": ["B", "B", "A", "A", "C", "C"], "Y": [1, 2, 3, 4, 5, 6], "Z": np.arange(10, 4, -1)})
print("===============原DataFrame=====================")
print(df)


===============原DataFrame=====================
   X  Y   Z
0  B  1  10
1  B  2   9
2  A  3   8
3  A  4   7
4  C  5   6
5  C  6   5
```



```python
print("==============匿名函数，将分组中的元素转为集合==================")
print(df.groupby('X').agg(lambda x: set(x)))
print("==============匿名函数联用 [lambda x: set(x), lambda x: x.quantile()]==================")
print(df.groupby('X').agg([lambda x: set(x), lambda x: x.quantile()]))
print("==============自定义函数，计算每组元素最大最小值的差值==================")
def diff(x):
    return max(x) - min(x)
print(df.groupby('X').agg(diff))



==============匿名函数，将分组中的元素转为集合==================
        Y        Z
X                 
A  {3, 4}   {8, 7}
B  {1, 2}  {9, 10}
C  {5, 6}   {5, 6}
==============匿名函数联用 [lambda x: set(x), lambda x: x.quantile()]==================
           Y                     Z           
  <lambda_0> <lambda_1> <lambda_0> <lambda_1>
X                                            
A     {3, 4}        3.5     {8, 7}        7.5
B     {1, 2}        1.5    {9, 10}        9.5
C     {5, 6}        5.5     {5, 6}        5.5
==============自定义函数，计算每组元素最大最小值的差值==================
   Y  Z
X      
A  1  1
B  1  1
C  1  1
```



### （3）应用多个函数到一列或多列

**对于如下的DataFrame**

```python
df = pd.DataFrame({"X": ["B", "B", "A", "A", "C", "C"], "Y": [1, 2, 3, 4, 5, 6], "Z": np.arange(10, 4, -1)})
print("===============原DataFrame=====================")
print(df)


===============原DataFrame=====================
   X  Y   Z
0  B  1  10
1  B  2   9
2  A  3   8
3  A  4   7
4  C  5   6
5  C  6   5

```



**对每个列都使用相同的聚合函数**

```python
gp_x = df.groupby('X')
print("==============对所有列求聚合 gp_x.agg(['sum', 'mean', 'count']))==================")
print(gp_x.agg(['sum', 'mean', 'count']))
print("==============单独对Y列求聚合 gp_x['Y'].agg(['sum', 'mean', 'count'])==================")
print(gp_x['Y'].agg(['sum', 'mean', 'count']))
print("==============对Y、Z两列求聚合 gp_x[['Y', 'Z']].agg(['sum', 'mean', 'count'])==================")
print(gp_x[['Y', 'Z']].agg(['sum', 'mean', 'count']))
print("==============单独对Y列求聚合，并且对列重命名 rename(column={聚合函数-》自定义名})==================")
print(gp_x['Y']
      .agg(['sum', 'mean', 'count'])
      .rename(columns={'sum': '求和', 'mean': '均值', 'count': '计数'}))



==============对所有列求聚合 gp_x.agg(['sum', 'mean', 'count']))==================
    Y              Z           
  sum mean count sum mean count
X                              
A   7  3.5     2  15  7.5     2
B   3  1.5     2  19  9.5     2
C  11  5.5     2  11  5.5     2
==============单独对Y列求聚合 gp_x['Y'].agg(['sum', 'mean', 'count'])==================
   sum  mean  count
X                  
A    7   3.5      2
B    3   1.5      2
C   11   5.5      2
==============对Y、Z两列求聚合 gp_x[['Y', 'Z']].agg(['sum', 'mean', 'count'])==================
    Y              Z           
  sum mean count sum mean count
X                              
A   7  3.5     2  15  7.5     2
B   3  1.5     2  19  9.5     2
C  11  5.5     2  11  5.5     2
==============单独对Y列求聚合，并且对列重命名 rename(column={聚合函数-》自定义名})==================
   求和   均值  计数
X             
A   7  3.5   2
B   3  1.5   2
C  11  5.5   2
```



**使用不同的函数到DataFrame不同的列**

```python
===============df.groupby('X').agg({'Y': 'max', 'Z': 'mean'})==========================
   Y    Z
X        
A  4  7.5
B  2  9.5
C  6  5.5
===============df.groupby('X').agg({'Z': 'max', 'Y': lambda x: x.quantile()})==========================
    Z    Y
X         
A   8  3.5
B  10  1.5
C   6  5.5
===============df.groupby('X').agg({'Y': ['max', 'mean'], 'Z': 'mean'})==========================
    Y         Z
  max mean mean
X              
A   4  3.5  7.5
B   2  1.5  9.5
C   6  5.5  5.5

```



### （4）Named Aggreation

​		**通过控制输出列名来支持特定列的聚合，pandas在`DataFrameGroupBy.agg()`和`SeriesGroupBy.agg()`中接受特殊的语法，被称为"命名聚合"，其中**

- **输出列名是关键字**
- **其对应的值是元组，元组的第一个值为操作的列，第二个值是对这列做的聚合操作。Pandas使用`['columns', 'aggfunc']`字段提供了`NamedAgg`的命名元组，以便清晰理解参数的含义，通常，聚合函数可以是一个callable或字符串别名**

**NamedAgg是NamedTuple的子类，其构造函数为 ==NamedAgg(column, aggfunc)==**

- **column：必须是Hashable**
- **aggfunc：func或str，必须是聚合函数**



**对于如下的DataFrame**

```python
df = pd.DataFrame({"X": ["B", "B", "A", "A", "C", "C"], "Y": [1, 2, 3, 4, 5, 6], "Z": np.arange(10, 4, -1)})
print("===============原DataFrame=====================")
print(df)


===============原DataFrame=====================
   X  Y   Z
0  B  1  10
1  B  2   9
2  A  3   8
3  A  4   7
4  C  5   6
5  C  6   5
```



```python
gp_x = df.groupby('X')
namedA1 = pd.NamedAgg(column='Y', aggfunc='sum')
namedA2 = pd.NamedAgg(column='Z', aggfunc=lambda x: sum(x) + 2)
print("===================传入两个NamedAgg,对Y求和，对Z求和再+2==================")
print(gp_x.agg(Y_sum = namedA1, Z_sum_2 = namedA2))
print("===================传入两个元组，对Y求和列名指定为Y_sum,对Z求均值,列名指定为Z_mean=================")
print(gp_x.agg(Y_sum = ('Y', 'sum'), Z_mean = ('Z', 'mean')))
print("===================SeriesGroupBy调用==================")
print(gp_x['Y'].agg(max_Y='max', min_Y = 'min'))



===================传入两个NamedAgg,对Y求和，对Z求和再+2==================
   Y_sum  Z_sum_2
X                
A      7       17
B      3       21
C     11       13
===================传入两个元组，对Y求和列名指定为Y_sum,对Z求均值,列名指定为Z_mean=================
   Y_sum  Z_mean
X               
A      7     7.5
B      3     9.5
C     11     5.5
===================SeriesGroupBy调用==================
   max_Y  min_Y
X              
A      4      3
B      2      1
C      6      5
```



**<span style='color: red;fontg-size: 19px'>如果你想指定的列名不是Python的有效语法，请构造一个字典并解包关键字参数</span>**

```python
print("=================== **kwarg 解包，如果列名不是Python的有效语法 ==================")
print(gp_x.agg(**{
    'total Y': pd.NamedAgg(column='Y', aggfunc='sum')
}))


=================== **kwarg 解包，如果列名不是Python的有效语法 ==================
   total Y
X         
A        7
B        3
C       11
```



## 3、转换（`Transformation`）

**转换操作会对每个组应用一个函数，然后返回一个与原始数据相同形状的结果，最常见的用途是将转换的结果添加到原数据中**

```python
In [117]: speeds
Out[117]: 
          class           order  max_speed
falcon     bird   Falconiformes      389.0
parrot     bird  Psittaciformes       24.0
lion     mammal       Carnivora       80.2
monkey   mammal        Primates        NaN
leopard  mammal       Carnivora       58.0


In [121]: result = speeds.copy()

In [122]: result["cumsum"] = grouped.cumsum()

In [123]: result["diff"] = grouped.diff()

In [124]: result
Out[124]: 
          class           order  max_speed  cumsum   diff
falcon     bird   Falconiformes      389.0   389.0    NaN
parrot     bird  Psittaciformes       24.0   413.0 -365.0
lion     mammal       Carnivora       80.2    80.2    NaN
monkey   mammal        Primates        NaN     NaN    NaN
leopard  mammal       Carnivora       58.0   138.2    NaN
```



**内置的转换函数**

|        函数名        |          说明          |
| :------------------: | :--------------------: |
|  `bfill()/ffill()`   |  向后/向前填充缺失值   |
| `cumsum()/cumprod()` |    累加和/累积乘积     |
| `cummax()/cummin()`  |    累积最大/最小值     |
|     `cumcount()`     |        累积计数        |
|       `diff()`       | 每个组两个临近值的差值 |
|    `pct_change()`    |       百分比变化       |
|       `rank()`       |          排名          |
|      `shift()`       | 上移或下移每个组的元素 |



## 4、过滤（`Filter`）

**根据条件去过滤数据，使用filter方法，大部分情况下，传入用户自定义的函数**

```python
In [186]: sf = pd.Series([1, 1, 2, 3, 3, 3])

In [187]: sf.groupby(sf).filter(lambda x: x.sum() > 2)
Out[187]: 
3    3
4    3
5    3
dtype: int64


In [188]: dff = pd.DataFrame({"A": np.arange(8), "B": list("aabbbbcc")})

In [189]: dff.groupby("B").filter(lambda x: len(x) > 2)
Out[189]: 
   A  B
2  2  b
3  3  b
4  4  b
5  5  b

In [191]: dff["C"] = np.arange(8)

In [192]: dff.groupby("B").filter(lambda x: len(x["C"]) > 2)
Out[192]: 
   A  B  C
2  2  b  2
3  3  b  3
4  4  b  4
5  5  b  5
```





## 5、灵活的apply函数

```python
df = pd.DataFrame({"X": ["B", "B", "A", "A", "C", "C"], "Y": [1, 2, 3, 4, 5, 6], "Z": np.arange(10, 4, -1)})
print("===============原DataFrame=====================")
print(df)


===============原DataFrame=====================
   X  Y   Z
0  B  1  10
1  B  2   9
2  A  3   8
3  A  4   7
4  C  5   6
5  C  6   5



gp_x = df.groupby('X')
print("============对分组数据输出描述性信息==================")
print(gp_x['Y'].apply(lambda x: x.describe()))
print("============自定义函数==================")
def foo(x):
    return pd.DataFrame({
        "原数据": x,
        "x - avg": x - x.mean()
    })
print(gp_x['Z'].apply(foo))



============对分组数据输出描述性信息==================
X       
A  count    2.000000
   mean     3.500000
   std      0.707107
   min      3.000000
   25%      3.250000
   50%      3.500000
   75%      3.750000
   max      4.000000
B  count    2.000000
   mean     1.500000
   std      0.707107
   min      1.000000
   25%      1.250000
   50%      1.500000
   75%      1.750000
   max      2.000000
C  count    2.000000
   mean     5.500000
   std      0.707107
   min      5.000000
   25%      5.250000
   50%      5.500000
   75%      5.750000
   max      6.000000
Name: Y, dtype: float64
============自定义函数==================
     原数据  x - avg
X                
A 2    8      0.5
  3    7     -0.5
B 0   10      0.5
  1    9     -0.5
C 4    6      0.5
  5    5     -0.5
```





```python
df = pd.DataFrame(
    {
        "a": [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
        "b": [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        "c": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        "d": [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    }
)

#对a分组后，b列值的总和 以及 c列值的均值
def compute_matrix(grouper):
    result_dict = {'b_sum': grouper['b'].sum(), 'c_mean': grouper['c'].mean()}
    return pd.Series(result_dict)
print(df.groupby('a').apply(compute_matrix, include_groups=False))

   b_sum  c_mean
a               
0    2.0     0.5
1    2.0     0.5
2    2.0     0.5
```



## **:heavy_exclamation_mark:GroupBy示例**

**[原CSV文件](G:\01作业\Pandas\0620文件读取练习)，某招聘网站数据.csv**

```python
# todo: groupby练习
import pandas as pd
df = pd.read_csv("./examples/某招聘网站数据.csv",parse_dates=['createTime'])
# 1 - 分组统计｜均值
print("=========计算各区(district)的薪资(salary)均值============")
gp_dis = df.groupby('district')
gp_dis_sal_mean = gp_dis.agg({'salary': 'mean'})
print(gp_dis_sal_mean)
# 2 - 分组统计｜取消索引
print("===========重新按照上一题要求进行分组，但不使用 district 做为索引==============")
print(df.groupby('district', as_index=False)['salary'].agg('mean'))
# 3 - 分组统计｜排序
print("=========计算并提取平均薪资最高的区===========")
gp_dis_sort_sal = gp_dis.salary.agg('mean').sort_values(ascending=False)
print(gp_dis_sort_sal.iloc[0])
# 4 - 分组统计｜频率
print("===========计算不同行政区(district)，不同规模公司(companySize)出现的次数=============")
gp_dis_coms = df.groupby(['district', 'companySize'])
gp_dis_coms_count = gp_dis_coms['positionId'].agg('count')
print(gp_dis_coms_count)
# 5 - 分组统计｜修改索引名
# 将上一题的索引名修改为
# district -> 行政区
# companySize -> 公司规模
print("===========修改索引名=============")
print(gp_dis_coms_count.index.rename({'district': '行政区', 'companySize': '公司规模'}))
# 6 - 分组统计｜计数
print("============每个区出现的公司数量=============")
print(gp_dis.agg({'companyId': 'count'}))
# 7 - 分组查看｜全部
print("==============将数据按照 district、salary 进行分组，并查看各分组的行索引=================")
gp_dis_sal = df.groupby(['district', 'salary'])
for k, v in gp_dis_sal.indices.items():
    print(k, end=" ")
    print(v)
# 8 - 分组查看｜指定
print("=========将数据按照 district、salary 进行分组，并查看西湖区薪资为 30000 的工作==========")
print(gp_dis_sal.get_group(("西湖区", 30000))[["positionId", "positionName", "district", "salary"]])
# 9 - 分组规则｜通过匿名函数1
print("===========根据 createTime 列，计算每天不同 行政区 的发布的岗位数量=============")
gp_day_dis = df.groupby([df['createTime'].apply(lambda x: x.day), 'district'])
gp_day_dis_pos_count = gp_day_dis['positionId'].agg('count')
print(gp_day_dis_pos_count)
# 10 - 分组规则｜通过匿名函数2
print("=========计算各行政区的企业领域（industryField）包含电商的总数==========")
print(gp_dis['industryField'].agg(lambda x: x.str.contains('电商').sum()))
# 11 - 分组规则｜通过内置函数
print("============通过 positionName 的长度进行分组，并计算不同长度岗位名称的薪资均值===========")
print(df.groupby(df['positionName'].apply(lambda x: len(x)))['salary'].agg('mean'))
# 12 - 分组规则｜通过多列
print("==========计算不同 工作年限（workYear）和 学历（education）之间的薪资均值==============")
print(df.groupby(['workYear', 'education'])['salary'].agg('mean'))
# 13 - 聚合统计
print("===========分组计算不同行政区，薪水的最小值、最大值和平均值============")
print(gp_dis['salary'].agg(['max', 'min', 'mean']))
# 14 - 聚合统计｜自定义函数
print("===========在 上一题的基础上，在聚合计算时新增一列计算最大值与平均值的差值==========")
print(gp_dis['salary'].agg(['max', 'min', 'mean', lambda x: x.max() - x.mean()]))
# 15 -聚合统计｜多层
print("===========对不同行政区进行分组，并统计薪水的均值、中位数、标准差，以及得分的均值===============")
print(gp_dis.agg({
    'salary': ['mean', 'median', 'std'],
    'score': 'mean'
}))





=========计算各区(district)的薪资(salary)均值============
                salary
district              
上城区       26250.000000
下沙        30000.000000
余杭区       33583.333333
拱墅区       28500.000000
江干区       25250.000000
滨江区       31428.571429
萧山区       36250.000000
西湖区       30893.939394
===========重新按照上一题要求进行分组，但不使用 district 做为索引==============
  district        salary
0      上城区  26250.000000
1       下沙  30000.000000
2      余杭区  33583.333333
3      拱墅区  28500.000000
4      江干区  25250.000000
5      滨江区  31428.571429
6      萧山区  36250.000000
7      西湖区  30893.939394
=========计算并提取平均薪资最高的区===========
36250.0
===========计算不同行政区(district)，不同规模公司(companySize)出现的次数=============
district  companySize
上城区       50-150人         2
下沙        150-500人        1
余杭区       150-500人       13
          2000人以上        14
          50-150人         7
          500-2000人       2
拱墅区       2000人以上         1
          50-150人         1
          500-2000人       2
江干区       2000人以上         2
          500-2000人       2
滨江区       150-500人       14
          2000人以上         6
          500-2000人       1
萧山区       50-150人         1
          500-2000人       3
西湖区       15-50人          1
          150-500人        7
          2000人以上        11
          50-150人         5
          500-2000人       9
Name: positionId, dtype: int64
===========修改索引名=============
MultiIndex([('上城区',   '50-150人'),
            ( '下沙',  '150-500人'),
            ('余杭区',  '150-500人'),
            ('余杭区',   '2000人以上'),
            ('余杭区',   '50-150人'),
            ('余杭区', '500-2000人'),
            ('拱墅区',   '2000人以上'),
            ('拱墅区',   '50-150人'),
            ('拱墅区', '500-2000人'),
            ('江干区',   '2000人以上'),
            ('江干区', '500-2000人'),
            ('滨江区',  '150-500人'),
            ('滨江区',   '2000人以上'),
            ('滨江区', '500-2000人'),
            ('萧山区',   '50-150人'),
            ('萧山区', '500-2000人'),
            ('西湖区',    '15-50人'),
            ('西湖区',  '150-500人'),
            ('西湖区',   '2000人以上'),
            ('西湖区',   '50-150人'),
            ('西湖区', '500-2000人')],
           names=['行政区', '公司规模'])
============每个区出现的公司数量=============
          companyId
district           
上城区               2
下沙                1
余杭区              36
拱墅区               4
江干区               4
滨江区              21
萧山区               4
西湖区              33
==============将数据按照 district、salary 进行分组，并查看各分组的行索引=================
('上城区', 22500) [81]
('上城区', 30000) [97]
('下沙', 30000) [31]
('余杭区', 7500) [84]
('余杭区', 20000) [ 52 103]
('余杭区', 22500) [23 51]
('余杭区', 25000) [62]
('余杭区', 27500) [24 49]
('余杭区', 29000) [93]
('余杭区', 30000) [ 4 10 13 18 59 61 65 68 74 76 86 92 94]
('余杭区', 35000) [101]
('余杭区', 37500) [ 0 32 38 39 41]
('余杭区', 40000) [60 87]
('余杭区', 45000) [25]
('余杭区', 50000) [ 5 64 90]
('余杭区', 60000) [ 8 82]
('拱墅区', 24000) [72]
('拱墅区', 30000) [54 89 96]
('江干区', 3500) [2]
('江干区', 22500) [45]
('江干区', 30000) [73]
('江干区', 45000) [3]
('滨江区', 7500) [83]
('滨江区', 15000) [1]
('滨江区', 20000) [21 40]
('滨江区', 22500) [37]
('滨江区', 30000) [ 22  53  55  58  67  80 102]
('滨江区', 32500) [26]
('滨江区', 37500) [17 28 57 77]
('滨江区', 42500) [91]
('滨江区', 45000) [43 47]
('滨江区', 50000) [44]
('萧山区', 25000) [100]
('萧山区', 30000) [6]
('萧山区', 45000) [66 69]
('西湖区', 6500) [71]
('西湖区', 20000) [12]
('西湖区', 21500) [104]
('西湖区', 22500) [48 70]
('西湖区', 24000) [42]
('西湖区', 25000) [56]
('西湖区', 26500) [78]
('西湖区', 27000) [75]
('西湖区', 27500) [15 20 50 63]
('西湖区', 30000) [11 27 33 34 85 88 98]
('西湖区', 35000) [7]
('西湖区', 36500) [99]
('西湖区', 37500) [14 16 19 30 36 79 95]
('西湖区', 40000) [ 9 35]
('西湖区', 45000) [29 46]
=========将数据按照 district、salary 进行分组，并查看西湖区薪资为 30000 的工作==========
    positionId      positionName district  salary
11     6847013  大数据分析工程师(J11108)      西湖区   30000
27     5520623            数据分析经理      西湖区   30000
33     6764017         数据分析师（社招）      西湖区   30000
34     6228290           商业数据分析师      西湖区   30000
85     6792091           高级数据分析师      西湖区   30000
88     6597345           资深数据分析师      西湖区   30000
98     6655562         数据分析建模工程师      西湖区   30000
===========根据 createTime 列，计算每天不同 行政区 的发布的岗位数量=============
createTime  district
9           余杭区          1
10          拱墅区          1
11          萧山区          1
            西湖区          1
12          上城区          1
13          西湖区          1
14          余杭区          1
            拱墅区          1
            滨江区          1
            西湖区          3
15          余杭区          6
            滨江区          2
            西湖区          1
16          上城区          1
            下沙           1
            余杭区         28
            拱墅区          2
            江干区          4
            滨江区         18
            萧山区          3
            西湖区         27
Name: positionId, dtype: int64
=========计算各行政区的企业领域（industryField）包含电商的总数==========
district
上城区    0
下沙     1
余杭区    9
拱墅区    0
江干区    2
滨江区    9
萧山区    3
西湖区    4
Name: industryField, dtype: int64
============通过 positionName 的长度进行分组，并计算不同长度岗位名称的薪资均值===========
positionName
4     30125.000000
5     34083.333333
6     32954.545455
7     29816.666667
8     31875.000000
9     29375.000000
10    30000.000000
11    34166.666667
12    29583.333333
13    38833.333333
14    40000.000000
15    26000.000000
16    28750.000000
17    40000.000000
18    25750.000000
19    45000.000000
21    21500.000000
23    60000.000000
Name: salary, dtype: float64
==========计算不同 工作年限（workYear）和 学历（education）之间的薪资均值==============
workYear  education
1-3年      不限           36250.000000
          本科           31000.000000
          硕士           36875.000000
3-5年      不限           30312.500000
          大专           28125.000000
          本科           31828.125000
5-10年     不限           26250.000000
          本科           28423.076923
不限        不限           35000.000000
          本科           35625.000000
应届毕业生     不限           32500.000000
          本科           33833.333333
Name: salary, dtype: float64
===========分组计算不同行政区，薪水的最小值、最大值和平均值============
            max    min          mean
district                            
上城区       30000  22500  26250.000000
下沙        30000  30000  30000.000000
余杭区       60000   7500  33583.333333
拱墅区       30000  24000  28500.000000
江干区       45000   3500  25250.000000
滨江区       50000   7500  31428.571429
萧山区       45000  25000  36250.000000
西湖区       45000   6500  30893.939394
===========在 上一题的基础上，在聚合计算时新增一列计算最大值与平均值的差值==========
            max    min          mean    <lambda_0>
district                                          
上城区       30000  22500  26250.000000   3750.000000
下沙        30000  30000  30000.000000      0.000000
余杭区       60000   7500  33583.333333  26416.666667
拱墅区       30000  24000  28500.000000   1500.000000
江干区       45000   3500  25250.000000  19750.000000
滨江区       50000   7500  31428.571429  18571.428571
萧山区       45000  25000  36250.000000   8750.000000
西湖区       45000   6500  30893.939394  14106.060606
===========对不同行政区进行分组，并统计薪水的均值、中位数、标准差，以及得分的均值===============
                salary                             score
                  mean   median           std       mean
district                                                
上城区       26250.000000  26250.0   5303.300859   2.000000
下沙        30000.000000  30000.0           NaN   6.000000
余杭区       33583.333333  30000.0  10857.847721  15.166667
拱墅区       28500.000000  30000.0   3000.000000   2.750000
江干区       25250.000000  26250.0  17255.433927  39.250000
滨江区       31428.571429  30000.0  10445.436461  12.952381
萧山区       36250.000000  37500.0  10307.764064  18.250000
西湖区       30893.939394  30000.0   7962.566302   8.060606
```





# 八、访问器（Accessor）

​		**Pandas中的accessor是一种扩展机制，允许你为Series或DataFrame对象添加自定义功能，它们通过特定的命名空间（如`.str`，`.dt`，`.cat`等）提供特定类型数据的操作方法**



|         数据类型          |  访问器  |
| :-----------------------: | :------: |
| DateTime,Timedelta,Period |   `dt`   |
|          String           |  `str`   |
|        Categorical        |  `cat`   |
|          Sparse           | `sparse` |



|      Accessor      |             说明             |
| :----------------: | :--------------------------: |
|    `Series.str`    |  可以访问字符串的属性和方法  |
|    `Series.cat`    | 可以访问分类对象的属性和方法 |
|    `Series.dt`     | 可以访问日期时间的属性和方法 |
|  `Serise.sparse`   |     稀疏数据类型的访问器     |
| `DataFrame.sparse` |  SparseFrameAccessor的别名   |
|    `Index.str`     |        用于字符串操作        |



## 1、`.str`访问器

### （1）基础操作 ###

```python
s.str.lower()       # 转换为全小写
s.str.upper()       # 转换为全大写
s.str.title()       # 每个单词首字母大写
s.str.capitalize()  # 字符串首字母大写
s.str.swapcase()    # 大小写互换
s.str.strip()       # 去除两端空白
s.str.strip('chars')   # 去除指定字符
s.str.lstrip()      # 去除左端空白
s.str.rstrip()      # 去除右端空白
s.str.pad(width, side='left', fillchar=' ')  	# 填充到指定宽度
s.str.center(width, fillchar=' ') 	 # 居中填充
s.str.zfill(width)  # 用0左填充(常用于数字字符串)
s.str.isalpha()     # 是否全为字母
s.str.isnumeric()   # 是否全为数字
s.str.isalnum()     # 是否只含字母和数字
s.str.isdigit()     # 是否全为数字(更严格)
s.str.islower()     # 是否全小写
s.str.isupper()     # 是否全大写
s.str.isspace()     # 是否全为空白
s.str.isdecimal()   # 是否全为十进制数字
s.str.len()            # 计算字符串长度
s.str.repeat(repeats)  # 重复字符串
s.str.encode(encoding) # 编码
s.str.decode(encoding) # 解码
s.str.get(i)           # 获取第i个元素(拆分后)
s.str.cat(others=None, sep=None, na_rep=None)  # 连接字符串
s.str.join(sep)         # 用分隔符连接序列元素
```



### （2）字符串匹配

#### Index/Series.str.contains

**==Index/Series.str.contains(*pat, case=True, flags=0, na=\<no_default>, regex=True*)==**

​	**判断Series或index里的字符串是否包含指定的*pattern*或*regex*，这将返回一个布尔的Series或Index对象**



| 参数： |
| ------ |

**①pat：str**

​	**字符序列或正则表达式**

**②case：bool，默认True**

​	**如果为True，则大小写敏感**

**③flags：int，默认0**

​	**传递给Python的re模块的flags，例如`re.IGNORECASE`**

**④na：标量，可选**

​	**用于填充缺失值的值**

**⑤regex：bool，默认True**

​	**如果为True，则pat参数为正则表达式；如果为False，则把pat当作一个字符串的字面量**



| 返回值： |
| -------- |

**:arrow_right:布尔值的Series或Index**

​	**如果包含，则为True，否则为False**



**:a:Series调用**

```python
ser = pd.Series(['Mouse', 'dog', 'house and parrot', '23', np.nan])
print("============原Series=================")
print(ser)
print("============判断Series的每个值是否包含 ou 字符串=================")
print(ser.str.contains("ou", regex=False))
print("============判断Series的每个值是否包含整数=================")
print(ser.str.contains(r"\d", regex=True))
print("============判断Series的每个值是否包含整数，并把缺失值填充为False=================")
print(ser.str.contains(r"\d", regex=True, na=False))
print("============判断Series的每个值是否以M开头，后面是多个字母数字下划线组成 ^M\\w+=================")
print(ser.str.contains(r"^M\w+", regex=True))
print("============判断Series的每个值是否包含mouse或dog，指定大小写不敏感=================")
print(ser.str.contains(r"mouse|dog", case=False, regex=True))



#输出结果如下
============原Series=================
0               Mouse
1                 dog
2    house and parrot
3                  23
4                 NaN
dtype: object
============判断Series的每个值是否包含 ou 字符串=================
0     True
1    False
2     True
3    False
4      NaN
dtype: object
============判断Series的每个值是否包含整数=================
0    False
1    False
2    False
3     True
4      NaN
dtype: object
============判断Series的每个值是否包含整数，并把缺失值填充为False=================
0    False
1    False
2    False
3     True
4    False
dtype: bool
============判断Series的每个值是否以M开头，后面是多个字母数字下划线组成 ^M\w+=================
0     True
1    False
2    False
3    False
4      NaN
dtype: object
============判断Series的每个值是否包含mouse或dog，指定大小写不敏感=================
0     True
1     True
2    False
3    False
4      NaN
dtype: object
```



**:b:Index调用**

```python
ind = pd.Index(['apple', 'Pear', 'BANANA', 'pinapple', np.nan])
print("================原Index================")
print(ind)
print("================判断Index中的每个元素是否包含 ap 字符串================")
print(ind.str.contains('ap', regex=False))
print("================判断Index中的每个元素是否以p开头，后面是字母数字下划线 ^p\\w+ case=False================")
print(ind.str.contains(r'^p\w+', case=False, regex=False))
print("================与上一行等价，正则表达式为 ^p\\w+ flags=re.IGNORECASE================")
print(ind.str.contains(r'^p\w+', regex=False, flags=re.IGNORECASE))


#输出结果如下
================原Index================
Index(['apple', 'Pear', 'BANANA', 'pinapple', nan], dtype='object')
================判断Index中的每个元素是否包含 ap 字符串================
Index([True, False, False, True, nan], dtype='object')
================判断Index中的每个元素是否以p开头，后面是字母数字下划线 ^p\w+ case=False================
Index([False, False, False, False, nan], dtype='object')
================与上一行等价，正则表达式为 ^p\w+ flags=re.IGNORECASE================
Index([False, False, False, False, nan], dtype='object')
```



#### Series.str.find/rfind

**==Series.str.find/rfind(*sub, start=0, end=None*)==**

​	**返回 子字符串*sub* 在Series或Index的每个字符串元素中最小/最大的索引，如果没有找到，则返回`-1`**

​	**sub：str，要寻找的子字符串；start、end：开始和结束的索引位置**



```python
>>> ser = pd.Series(["cow_", "duck_", "do_ve"])
>>> ser.str.find("_")
0   3
1   4
2   2
dtype: int64


>>> ser = pd.Series(["_cow_", "duck_", "do_v_e"])
>>> ser.str.rfind("_")
0   4
1   4
2   4
dtype: int64
```





#### Series.str.findall

**==Series.str.findall(*pat, flags=0*)==**

​	**在Series或Index中找到所有出现的pattern或正则表达式，等价于对Series或Index的所有元素应用`re.findall()`**

​	**其中pat为字符串或正则表达式，flags为Python中re模块的flags，例如`re.IGNORECASE`**

​	**此函数返回所有非重叠的匹配对象**



```python
s = pd.Series(['Lion', 'Monkey', 'Rabbit'])
print("================原Series===========================")
print(s)
print("================找到所有的monkey，flags设置为re.IGNORECASE===========================")
print(s.str.findall("monkey", flags=re.IGNORECASE))
print("================找到所有的on===========================")
print(s.str.findall("on"))
print("================找到所有的b===========================")
print(s.str.findall("b"))



#输出结果如下
================原Series===========================
0      Lion
1    Monkey
2    Rabbit
dtype: object
================找到所有的monkey，flags设置为re.IGNORECASE===========================
0          []
1    [Monkey]
2          []
dtype: object
================找到所有的on===========================
0    [on]
1    [on]
2      []
dtype: object
================找到所有的b===========================
0        []
1        []
2    [b, b]
dtype: object
```



#### Series.str.match

**==Series.str.match(*pat, case=True, flags=0, na=\<no_default>*)==**

​	**判断Series或Index的每个字符串元素是否与指定的正则表达式匹配**

​	**pat: str，字符序列；case：指定是否大小写敏感；flags：Python中re模块的flags；na：指定替换缺失值的值**

​	**该函数返回一个布尔值的Series、Index或数组**



```python
>>> ser = pd.Series(["horse", "eagle", "donkey"])
>>> ser.str.match("e")
0   False
1   True
2   False
dtype: bool
```





### （3）字符串拆分与替换

#### Series.str.replace

**==Series.str.replace(*pat, repl, n=-1, case=None, flags=0, regex=False*)==**

​	**替换在Series或Index中所有出现的pattern或正则表达式，等价于Python的`re.sub()`**

​	**注意，当pat是已编译的正则表达式对象时，所有标志都应包含在已编译的正则表达式中，此时，再往函数中传递case、flags或regex=False将引发错误**



| 参数： |
| ------ |

**①pat：str 或 已编译的regex对象**

​	**能作为字符序列或正则表达式的字符串**

**②repl：str或callable**

​	**用于代替的字符串或callable，可调用对象必须传递一个正则表达式的匹配对象并且必须返回一个用于替代的字符串。**

**③n：int，默认-1（代替所有匹配的字符串）**

​	**指定替换字符串的次数**

**④case：bool，默认None**

​	**指定是否大小写敏感**

**⑤flags：int，默认0**

​	**Python中re模块的flags**

**⑥regex：bool，默认False**

​	**是否将传递的pat参数解析为正则表达式**



| 返回值： |
| -------- |

**:arrow_right:返回被repl替换了的Series或Index对象**



```python
>>> pd.Series(['foo', 'fuz', np.nan]).str.replace('f.', 'ba', regex=True)
0    bao
1    baz
2    NaN
dtype: object


>>> pd.Series(['f.o', 'fuz', np.nan]).str.replace('f.', 'ba', regex=False)
0    bao
1    fuz
2    NaN
dtype: object


# 反转每个小写字母
>>> repl = lambda m: m.group(0)[::-1]
>>> ser = pd.Series(['foo 123', 'bar baz', np.nan])
>>> ser.str.replace(r'[a-z]+', repl, regex=True)
0    oof 123
1    rab zab
2        NaN
dtype: object


# 使用正则表达式组，对于第二组，交换字母的大小写
>>> pat = r"(?P<one>\w+) (?P<two>\w+) (?P<three>\w+)"
>>> repl = lambda m: m.group('two').swapcase()
>>> ser = pd.Series(['One Two Three', 'Foo Bar Baz'])
>>> ser.str.replace(pat, repl, regex=True)
0    tWO
1    bAR
dtype: object


# pat参数使用正则表达式对象传入
>>> import re
>>> regex_pat = re.compile(r'FUZ', flags=re.IGNORECASE)
>>> pd.Series(['foo', 'fuz', np.nan]).str.replace(regex_pat, 'bar', regex=True)
0    foo
1    bar
2    NaN
dtype: object
```



#### Series.str.split/rsplit

**==Series.str.split/rsplit(*pat=None, n=-1, expand=False, regex=None*)==**

​	**根据给定的分隔符(pat参数)分隔字符串。特别的，`rsplit`表示从右侧开始拆分字符串**



| 参数： |
| ------ |

**①pat：str 或 已编译的regex对象，可选**

​	**指定使用什么分隔符拆分eries或Index中的字符串元素，默认使用空格**

**②n：int，默认-1（分隔所有）**

​	**指定最大分隔次数为n次，如果为0或-1，将返回所有分隔部分**

**③expand：bool，默认False**

​	**是否将分隔的字符串扩展为分开的列**

​	**如果为True，则返回DataFrame或MultiIndex；否则返回Series或Index**

**④regex：bool，默认False**

​	**是否将pat解析为正则表达式**



| 返回值： |
| -------- |

**:arrow_right:Series、Index、DataFrame或MultiIndex**

​	**与调用者类型相同。如果`expand=True`，返回类型不保证**





```python
s = pd.Series(
    [
        "this is a regular sentence",
        "org/reg/tutorial/index.html",
        np.nan
    ]
)
print("===========原Series==================")
print(s)
print("=============默认使用空格进行分隔，这与rsplit函数表现一样================")
print(s.str.split())
print("=============调用 s.str.rsplit()================")
print(s.str.rsplit())
print("=============默认使用空格进行分隔，指定最大分隔次数为两次================")
print(s.str.split(n=2))
print("=============默认使用空格进行分隔，指定最大分隔次数为两次,调用rsplit================")
print(s.str.rsplit(n=2))
print("=============指定使用's'进行分隔================")
print(s.str.split('s'))
print("=============默认使用空格进行分隔，指定expand = True================")
print(s.str.split(expand=True))
print("=============指定使用/进行分隔，分隔次数设置为1，expand = True================")
print(s.str.split('/', n=1, expand=True))
print("=============以r开头 后边跟2个字母数字或下划线 pat = r‘r\\w{2}’================")
print(s.str.split(r"r\w{2}", regex=True))



# 输出结果如下
===========原Series==================
0     this is a regular sentence
1    org/reg/tutorial/index.html
2                            NaN
dtype: object
=============默认使用空格进行分隔，这与rsplit函数表现一样================
0    [this, is, a, regular, sentence]
1       [org/reg/tutorial/index.html]
2                                 NaN
dtype: object
=============调用 s.str.rsplit()================
0    [this, is, a, regular, sentence]
1       [org/reg/tutorial/index.html]
2                                 NaN
dtype: object
=============默认使用空格进行分隔，指定最大分隔次数为两次================
0    [this, is, a regular sentence]
1     [org/reg/tutorial/index.html]
2                               NaN
dtype: object
=============默认使用空格进行分隔，指定最大分隔次数为两次,调用rsplit================
0    [this is a, regular, sentence]
1     [org/reg/tutorial/index.html]
2                               NaN
dtype: object
=============指定使用's'进行分隔================
0    [thi,  i,  a regular , entence]
1      [org/reg/tutorial/index.html]
2                                NaN
dtype: object
=============默认使用空格进行分隔，指定expand = True================
                             0     1     2        3         4
0                         this    is     a  regular  sentence
1  org/reg/tutorial/index.html  None  None     None      None
2                          NaN   NaN   NaN      NaN       NaN
=============指定使用/进行分隔，分隔次数设置为1，expand = True================
                            0                        1
0  this is a regular sentence                     None
1                         org  reg/tutorial/index.html
2                         NaN                      NaN
=============以r开头 后边跟2个字母数字或下划线 pat = r‘r\w{2}’================
0    [this is a , ular sentence]
1    [org/, /tuto, l/index.html]
2                            NaN
dtype: object
```





#### Series.str.slice

**==Series.str.slice(*start=None, stop=None, step=None*)==**

​	**对Series或Index中的字符串元素做切片**

​	**`Series.str.slice(start=0, stop=5, step=3)`等价于`s.str[0:5:3]`**





### （4）字符串提取

#### Series.str.extract

**==Series.str.extract(*pat, flags=0, expend=True*)==**

​	**将正则表达式pat中的捕获组提取为DataFrame中的列**



| 参数： |
| ------ |

**①pat：str**

​	**带有捕获组的正则表达式，即带有`()`，一个`()`代表一个捕获组**

**②flags：int，默认0**

​	**Python中re模块的flags**

**③expend：bool，默认为True**

​	**如果为True，则返回的每个捕获组占一列DataFrame。如果为False，若只有一个捕获组，则返回Series或Index，若有多个捕获组，则返回DataFrame**



```python
s = pd.Series(['a1', 'b2', 'c3'])
print("=================原Series===================")
print(s)
print("=================pat = r'([ab])(\\d)'===================")
print(s.str.extract(r'([ab])(\d)'))
print("=================pat = r'[ab](\\d)', expand=True,返回DataFrame===================")
a = s.str.extract(r'[ab](\d)', expand=True)
print(a, type(a))
print("=================pat = r'[ab](\\d)', expand=False,返回Series===================")
b = s.str.extract(r'[ab](\d)', expand=False)
print(b, type(b))



# 输出结果如下
=================原Series===================
0    a1
1    b2
2    c3
dtype: object
=================pat = r'([ab])(\d)'===================
     0    1
0    a    1
1    b    2
2  NaN  NaN
=================pat = r'[ab](\d)', expand=True,返回DataFrame===================
     0
0    1
1    2
2  NaN <class 'pandas.core.frame.DataFrame'>
=================pat = r'[ab](\d)', expand=False,返回Series===================
0      1
1      2
2    NaN
dtype: object <class 'pandas.core.series.Series'>
```





#### Series.str.get_dummies

**==Series.get_dummies(*sep='|'*)==**

​	**返回Series中字符串元素的虚拟变量的DataFrame，分隔符可以指定为任意字符串，默认分隔符为`|`**



```python
>>> pd.Series(['a|b', 'a', 'a|c']).str.get_dummies()
   a  b  c
0  1  1  0
1  1  0  0
2  1  0  1


>>> pd.Series(['a|b', np.nan, 'a|c']).str.get_dummies()
   a  b  c
0  1  1  0
1  0  0  0
2  1  0  1
```





## 2、`.cat`访问器

**分类对象的属性**

| 属性                                                         | 说明                         |
| :----------------------------------------------------------- | ---------------------------- |
| [`Series.cat.categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.categories.html#pandas.Series.cat.categories) | 分类对象的类别               |
| [`Series.cat.ordered`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.ordered.html#pandas.Series.cat.ordered) | 分类类别是否有序             |
| [`Series.cat.codes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.codes.html#pandas.Series.cat.codes) | 返回分类编码及其索引的Series |



**分类对象的方法**

| 方法                                                         | 说明                                                |
| ------------------------------------------------------------ | --------------------------------------------------- |
| [`Series.cat.rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.rename_categories.html#pandas.Series.cat.rename_categories)(*args, **kwargs) | Rename categories.                                  |
| [`Series.cat.reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.reorder_categories.html#pandas.Series.cat.reorder_categories)(*args, **kwargs) | 重新排序分类类别                                    |
| [`Series.cat.add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.add_categories.html#pandas.Series.cat.add_categories)(*args, **kwargs) | Add new categories.                                 |
| [`Series.cat.remove_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_categories.html#pandas.Series.cat.remove_categories)(*args, **kwargs) | Remove the specified categories.                    |
| [`Series.cat.remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_unused_categories.html#pandas.Series.cat.remove_unused_categories)(*args, ...) | Remove categories which are not used.               |
| [`Series.cat.set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.set_categories.html#pandas.Series.cat.set_categories)(*args, **kwargs) | Set the categories to the specified new categories. |
| [`Series.cat.as_ordered`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.as_ordered.html#pandas.Series.cat.as_ordered)(*args, **kwargs) | 分类类别转为有序                                    |
| [`Series.cat.as_unordered`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.as_unordered.html#pandas.Series.cat.as_unordered)(*args, **kwargs) | 分类类别转为无序                                    |





## 3、`.dt`访问器

### （1）DateTime

**基本属性**

```python
Series.dt.year      # 年份
Series.dt.month     # 月份 (1-12)
Series.dt.day       # 月份中的日 (1-31)
Series.dt.hour      # 小时 (0-23)
Series.dt.minute    # 分钟 (0-59)
Series.dt.second    # 秒 (0-59)
Series.dt.microsecond  # 微秒
Series.dt.nanosecond   # 纳秒


Series.dt.date         # 返回python datetime.date对象的NumPy数组
Series.dt.time         # 返回datetime.time对象的NumPy数组
Series.dt.timetz       # 返回带有时区的datetime.time对象的NumPy数组
Series.dt.dayofweek    # 一周中的第几天 (0-6, 0是周一)
Series.dt.weekday      # 同dayofweek (0-6, 0是周一)
Series.dt.dayofyear    # 一年中的第几天 (1-366)
Series.dt.days_in_month     # 当月有多少天
Series.dt.quarter     		 # 当前日期在第几季度 (1-4)
Series.dt.is_month_start  # 是否是当月第一天
Series.dt.is_month_end    # 是否是当月最后一天
Series.dt.is_quarter_start  # 是否是当季第一天
Series.dt.is_quarter_end    # 是否是当季最后一天
Series.dt.is_year_start     # 是否是当年第一天
Series.dt.is_year_end       # 是否是当年最后一天
Series.dt.is_leap_year		# 是否是闰年
Series.dt.tz				#返回时区

Series.dt.isocalendar().week  # ISO标准周数
```



**方法**

| 方法                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`Series.dt.isocalendar`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.isocalendar.html#pandas.Series.dt.isocalendar)() | 根据ISO 8601标准计算 year, week, and day                     |
| [`Series.dt.to_period`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_period.html#pandas.Series.dt.to_period)(*args, **kwargs) | 转成Period对象                                               |
| [`Series.dt.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz_localize.html#pandas.Series.dt.tz_localize)(*args, **kwargs) | 设置时区                                                     |
| [`Series.dt.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz_convert.html#pandas.Series.dt.tz_convert)(*args, **kwargs) | 转换时区                                                     |
| [`Series.dt.normalize`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.normalize.html#pandas.Series.dt.normalize)(*args, **kwargs) | 将时间设置为午夜，保留日期部分，将时间设置为00:00:00         |
| [`Series.dt.strftime`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.strftime.html#pandas.Series.dt.strftime)(*args, **kwargs) | 格式化日期为字符串                                           |
| [`Series.dt.round`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.round.html#pandas.Series.dt.round)(*args, **kwargs) | 四舍五入                                                     |
| [`Series.dt.floor`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.floor.html#pandas.Series.dt.floor)(*args, **kwargs) | 向下取整                                                     |
| [`Series.dt.ceil`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.ceil.html#pandas.Series.dt.ceil)(*args, **kwargs) | Perform ceil operation on the data to the specified freq.    |
| [`Series.dt.month_name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month_name.html#pandas.Series.dt.month_name)(*args, **kwargs) | 返回当前日期所在月（例如`'January', 'February', 'March'`）   |
| [`Series.dt.day_name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_name.html#pandas.Series.dt.day_name)(*args, **kwargs) | 返回当前日期所在星期（例如`'Monday', 'Tuesday', 'Wednesday'`） |
| [`Series.dt.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.as_unit.html#pandas.Series.dt.as_unit)(*args, **kwargs) |                                                              |





### （2）Period

| 属性                                                         | 说明                                           |
| :----------------------------------------------------------- | ---------------------------------------------- |
| [`Series.dt.start_time`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.start_time.html#pandas.Series.dt.start_time) | Get the Timestamp for the start of the period. |
| [`Series.dt.end_time`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.end_time.html#pandas.Series.dt.end_time) | Get the Timestamp for the end of the period.   |



### （3）Timedelta



| 属性                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`Series.dt.days`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.days.html#pandas.Series.dt.days) | Number of days for each element.                             |
| [`Series.dt.seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.seconds.html#pandas.Series.dt.seconds) | Number of seconds (>= 0 and less than 1 day) for each element. |
| [`Series.dt.microseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.microseconds.html#pandas.Series.dt.microseconds) | Number of microseconds (>= 0 and less than 1 second) for each element. |
| [`Series.dt.nanoseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.nanoseconds.html#pandas.Series.dt.nanoseconds) | Number of nanoseconds (>= 0 and less than 1 microsecond) for each element. |
| [`Series.dt.components`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.components.html#pandas.Series.dt.components) | Return a Dataframe of the components of the Timedeltas.      |
| [`Series.dt.unit`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.unit.html#pandas.Series.dt.unit) |                                                              |



| 方法                                                         | 说明                                                        |
| ------------------------------------------------------------ | ----------------------------------------------------------- |
| [`Series.dt.to_pytimedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_pytimedelta.html#pandas.Series.dt.to_pytimedelta)() | 返回本地的 `datetime.timedelta` 对象的数组                  |
| [`Series.dt.total_seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.total_seconds.html#pandas.Series.dt.total_seconds)(*args, **kwargs) | Return total duration of each element expressed in seconds. |
| [`Series.dt.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.as_unit.html#pandas.Series.dt.as_unit)(*args, **kwargs) |                                                             |





# 九、重塑和数据透视表

**Pandas提供了一些改变数据表现形式的方法，以便更好的对数据处理或汇总**

- **`pivot()`和`pivot_table()`：将唯一值分组到一个或多个离散类别中**
- **`stack()`和`unstack()`：分别将列或行级别旋转到相反的轴**
- **`melt()`和`wide_to_long()`：将宽格式的DataFrame转为长格式**
- **`get_dummies()`和`from_dummies()`：虚拟变量的转换**
- **`explode()`：将一列值转换为单独的行**
- **`crosstab()`：计算多个一维因子数组的交叉表，计算频率分布关系使用**
- **`cut()`和`qcut()`：分箱**
- **`factorize()`：将一维变量编码为整数标签**



## 1、`pivot()`和`pivot_table()`

<img src="G:\01资料\Pictures\reshaping_pivot.png" style="zoom:80%;" />



### pandas.pivot

**==pandas.pivot(*data, columns, index=\<no_default>, values=\<no_default>*)==**

​	**返回按给定索引或列的值 组织的一个新的DataFrame**

​	**基于列值重塑数据，生成数据透视表。使用指定索引/列中的唯一值来构成结果DataFrame的轴，此函数不支持数据聚合，多个值将导致列中出现多级索引（MultiIndex）**



| 参数： |
| ------ |

**①data：DataFrame**

**②columns: str 或 object 或 str的列表**

​	**用于构造新DataFrame列的列**

**③index：str 或 object 或 str的列表，可选**

​	**用于构造新DataFrame的索引的列，如果未提供，则使用现有索引**

**④values：str，object 或 前一个列表，可选**

​	**用于填充新DataFrame的值的列，如果为指定，则将使用所有剩余列，并且结果是具有按层次索引的列**



| 返回值： |
| -------- |

**:arrow_right:返回重塑的DataFrame**





### pandas.pivot_table

**==pandas.pivot_table(*data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='ALL', observed=True, sort=True*)==**

​	**创建电子表格样式的数据透视表作为DataFrame，数据透视表中的级别将存储在结果DataFrame的索引和列上的多级索引对象中**



| 参数： |
| ------ |

**①data：DataFrame**

**②values：类列表或标量，可选**

​	**列或要聚合的列**

**③index：column，Grouper，数组 或 前一个列表**

​	**数组透视表索引上分组的键。如果传递的是列表，它可以包含除列表之外的任何其他类型；如果传递的是数组，则数组的长度必须与数据长度相同**

**④columns：column，Grouper，数组或 前一个列表**

​	**数组透视表列上分组的键。如果传递的是列表，它可以包含除列表之外的任何其他类型；如果传递的是数组，则数组的长度必须与数据长度相同**

**⑤aggfunc：函数，函数列表，字典，默认'mean'**

​	**如果传递的是函数列表，则生成的数据透视表将包含分层列，其顶层是函数名称。**

​	**如果传递的是字典，则键是要聚合的列，值是函数或函数列表。**

​	**如果传递的是`margin=True`，则将使用aggfunc计算margin的值**

**⑥margins：bool，默认False**

​	**如果`margins=True`，则会添加所有特殊的行和列，并在行和列的类别中添加部分组聚合**

**⑦dropna：bool，默认为True**

​	**不包括所有条目均为NaN的列。如果为True，则在计算边距之前，任何列中具有NaN值的行都将被忽略**

**⑧margins_name：str，默认'All'**

​	**当`margins=True`时包含总计的行/列的名称**

**⑨fill_value：int**

​	**用于填充缺失值的值**

**⑩sort：bool，默认True**

​	**指定结果是否排序**



| 返回值： |
| -------- |

**:arrow_right:DataFrame：一个Excel风格的透视表**



### （1）`pivot()` 应用

**一个简单的透视例子**

```python
data = {
   "value": range(12),
   "variable": ["A"] * 3 + ["B"] * 3 + ["C"] * 3 + ["D"] * 3,
   "date": pd.to_datetime(["2020-01-03", "2020-01-04", "2020-01-05"] * 4)
}
df = pd.DataFrame(data)
print("===============原DataFrame==============")
print(df)
print("================== 简单透视 ====================")
print("============ df.pivot(index='date', columns='variable', values='value') ===============")
print(df.pivot(index='date', columns='variable', values='value'))
print("============== df.pivot(index='date', columns='variable') =================")
print(df.pivot(index='date', columns='variable'))


#输出结果如下
===============原DataFrame==============
    value variable       date
0       0        A 2020-01-03
1       1        A 2020-01-04
2       2        A 2020-01-05
3       3        B 2020-01-03
4       4        B 2020-01-04
5       5        B 2020-01-05
6       6        C 2020-01-03
7       7        C 2020-01-04
8       8        C 2020-01-05
9       9        D 2020-01-03
10     10        D 2020-01-04
11     11        D 2020-01-05
================== 简单透视 ====================
============ df.pivot(index='date', columns='variable', values='value') ===============
variable    A  B  C   D
date                   
2020-01-03  0  3  6   9
2020-01-04  1  4  7  10
2020-01-05  2  5  8  11
============== df.pivot(index='date', columns='variable') =================
           value          
variable       A  B  C   D
date                      
2020-01-03     0  3  6   9
2020-01-04     1  4  7  10
2020-01-05     2  5  8  11
```



**透视表为多级索引**

```python
df = pd.DataFrame({
       "lev1": [1, 1, 1, 2, 2, 2],
       "lev2": [1, 1, 2, 1, 1, 2],
       "lev3": [1, 2, 1, 2, 1, 2],
       "lev4": [1, 2, 3, 4, 5, 6],
       "values": [0, 1, 2, 3, 4, 5]})
print("===============原DataFrame==============")
print(df)
print("================== 多级索引的透视表 ====================")
print("================ df.pivot(index='lev1', columns=['lev2', 'lev3'], values='values') =====================")
print(df.pivot(index='lev1', columns=['lev2', 'lev3'], values='values'))
print("================ df.pivot(index=['lev1', 'lev2'], columns='lev3', values='values') =====================")
print(df.pivot(index=['lev1', 'lev2'], columns='lev3', values='values'))



#输出结果如下
===============原DataFrame==============
   lev1  lev2  lev3  lev4  values
0     1     1     1     1       0
1     1     1     2     2       1
2     1     2     1     3       2
3     2     1     2     4       3
4     2     1     1     5       4
5     2     2     2     6       5
================== 多级索引的透视表 ====================
================ df.pivot(index='lev1', columns=['lev2', 'lev3'], values='values') =====================
lev2    1         2     
lev3    1    2    1    2
lev1                    
1     0.0  1.0  2.0  NaN
2     4.0  3.0  NaN  5.0
================ df.pivot(index=['lev1', 'lev2'], columns='lev3', values='values') =====================
lev3         1    2
lev1 lev2          
1    1     0.0  1.0
     2     2.0  NaN
2    1     4.0  3.0
     2     NaN  5.0
```





### （2）`pivot_table()` 应用

**<span style='color: red;font-size: 19px'>注意：</span>`pivot()`仅仅可以处理由`index`和`columns`决定的唯一行，如果数据包含重复值，使用`pivot_table()`，重复值默认会用平均值填充**

**例如：下述的DataFrame中，'foo'中的one和'bar'中的A对应了baz中不同的值，所以会发生[ValueError][]**

```python
df = pd.DataFrame({"foo": ['one', 'one', 'two', 'two'],
                   "bar": ['A', 'A', 'B', 'C'],
                   "baz": [1, 2, 3, 4]})
>>> print(df)
   foo bar  baz
0  one   A    1
1  one   A    2
2  two   B    3
3  two   C    4



>>> df.pivot(index='foo', columns='bar', values='baz')
ValueError: Index contains duplicate entries, cannot reshape
```





```python
df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
>>> print(df)
     A    B      C  D  E
0  foo  one  small  1  2
1  foo  one  large  2  4
2  foo  one  large  2  5
3  foo  two  small  3  5
4  foo  two  small  3  6
5  bar  one  large  4  6
6  bar  one  small  5  8
7  bar  two  small  6  9
8  bar  two  large  7  9


# 普通透视表，通过行和列锁定的值如果重复，则默认使用平均值填充，因为aggfunc='mean'
>>> print(pd.pivot_table(df, index=['A', 'B'], columns=['C'], values=['D', 'E']))
            D           E      
C       large small large small
A   B                          
bar one   4.0   5.0   6.0   8.0
    two   7.0   6.0   9.0   9.0
foo one   2.0   1.0   4.5   2.0
    two   NaN   3.0   NaN   5.5

    
# 填充缺失值为0
>>> print(pd.pivot_table(df, index=['A', 'B'], columns=['C'], values=['D', 'E'], fill_value=0))
            D           E      
C       large small large small
A   B                          
bar one   4.0   5.0   6.0   8.0
    two   7.0   6.0   9.0   9.0
foo one   2.0   1.0   4.5   2.0
    two   0.0   3.0   0.0   5.5

    
# 通过index和columns锁定的重复值 求和
>>> print(pd.pivot_table(df, index=['A', 'B'], columns=['C'], values=['D', 'E'], aggfunc='sum', fill_value=0))
            D           E      
C       large small large small
A   B                          
bar one     4     5     6     8
    two     7     6     9     9
foo one     4     1     9     2
    two     0     6     0    11

    
# 对于给定列计算多种不同类型的聚合
>>> print(pd.pivot_table(df, index=['A', 'B'], 
                         	values=['D', 'E'], 
                         	aggfunc={'D': ['max', 'min', 'median'],
                                     'E': 'std'}, fill_value=0))   
          D                    E
        max median min       std
A   B                           
bar one   5    4.5   4  1.414214
    two   7    6.5   6  0.000000
foo one   2    2.0   1  1.527525
    two   3    3.0   3  0.707107
```



**index或columns传`Grouper`对象**

```python
df = pd.DataFrame(
    {
        "date": [datetime.datetime(2013, i, 1) for i in range(1, 13)],
        "foo": ['a', 'b', 'c'] * 4,
        "bar": np.random.uniform(2, 6, 12).round(3)
    }
)
>>> print(df)

         date foo    bar
0  2013-01-01   a  2.043
1  2013-02-01   b  2.746
2  2013-03-01   c  3.269
3  2013-04-01   a  5.153
4  2013-05-01   b  2.549
5  2013-06-01   c  3.892
6  2013-07-01   a  4.893
7  2013-08-01   b  5.732
8  2013-09-01   c  2.045
9  2013-10-01   a  3.949
10 2013-11-01   b  3.752
11 2013-12-01   c  2.994


>>> print(df.pivot_table(index=pd.Grouper(key='date', freq='ME'), columns='foo', values='bar'))
foo             a      b      c
date                           
2013-01-31  2.043    NaN    NaN
2013-02-28    NaN  2.746    NaN
2013-03-31    NaN    NaN  3.269
2013-04-30  5.153    NaN    NaN
2013-05-31    NaN  2.549    NaN
2013-06-30    NaN    NaN  3.892
2013-07-31  4.893    NaN    NaN
2013-08-31    NaN  5.732    NaN
2013-09-30    NaN    NaN  2.045
2013-10-31  3.949    NaN    NaN
2013-11-30    NaN  3.752    NaN
2013-12-31    NaN    NaN  2.994
```



​		**`pivot_table()`可以传递`margins=True`，这将为生成的DataFrame加一个边，即在最右边新加一列且最下边新加一行，其行/列标签均为`margins_name`，其中的值为根据的`aggfunc`参数传递的聚合函数计算出来的。**

​		**也就是说，例如：对于`aggfunc='sum'`且`margins=True`, 则生成的透视表添加的边为每列/行的累加和（`sum`），其 边 的标签名为`margins_name`**

```python
df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
print(df)
print("==================margin = True，给生成的DataFrame加边，其结果默认为每行/列平均值======================")
print(pd.pivot_table(df[['A', 'B', 'C', 'D']],
                     index=['A', 'B'],
                     columns='C',
                     values='D',
                     fill_value=0,
                     margins=True))
print("==================margin = True，给生成的DataFrame加边，指定为 每行/列求和的结果======================")
print(pd.pivot_table(df[['A', 'B', 'C', 'D']],
                     index=['A', 'B'],
                     columns='C',
                     values='D',
                     fill_value=0,
                     margins=True,
                     aggfunc='sum'))
print("==================margin = True，给生成的DataFrame加边，指定为 每行/列的标准差，标签名指定为std======================")
print(pd.pivot_table(df[['A', 'B', 'C', 'D']],
                     index=['A', 'B'],
                     columns='C',
                     values='D',
                     fill_value=0,
                     margins=True,
                     margins_name="std",
                     aggfunc='std'))



#输出结果如下
     A    B      C  D  E
0  foo  one  small  1  2
1  foo  one  large  2  4
2  foo  one  large  2  5
3  foo  two  small  3  5
4  foo  two  small  3  6
5  bar  one  large  4  6
6  bar  one  small  5  8
7  bar  two  small  6  9
8  bar  two  large  7  9
==================margin = True，给生成的DataFrame加边，其结果默认为每行/列平均值======================
C        large  small       All
A   B                          
bar one   4.00    5.0  4.500000
    two   7.00    6.0  6.500000
foo one   2.00    1.0  1.666667
    two   0.00    3.0  3.000000
All       3.75    3.6  3.666667
==================margin = True，给生成的DataFrame加边，指定为 每行/列求和的结果======================
C        large  small  All
A   B                     
bar one      4      5    9
    two      7      6   13
foo one      4      1    5
    two      0      6    6
All         15     18   33
==================margin = True，给生成的DataFrame加边，指定为 每行/列的标准差，标签名指定为std======================
C           large     small      std
A   B                               
foo one  0.000000  0.000000  0.57735
    two  0.000000  0.000000  0.00000
std      2.362908  1.949359  2.00000
```





## 2、`stack()`和`unstack()`

**`pivot()`方法和`stack()`和`unstack()`相关，这些方法被设计与多级索引对象协同使用**

- **`stack()`：对列标签的某一级别进行透视，返回一个带有最内层的行标签索引的DataFrame**
- **`unstack()`：`stack()`的逆操作，将某一级别的行索引旋转到列轴，生成一个重塑的DataFrame，列标签是原先DataFrame的最内层的行索引**





### DataFrame.stack

**==DataFrame.stack(*level=-1, dropna=\<no_default>, sort=\<no_default>, future_stack=False*)==**

​	**按指定的级别从列堆叠到索引**

​	**该方法返回一个重塑后的DataFrame或Series，该DataFrame或Series具有多级索引，与当前的DataFrame相比，新增了一个或多个最内层级，新的最内层级是通过旋转当前DataFrame的列创建的：**

- **如果列只有一个级别，则输出为Series**
- **如果列有多个级别，则新的索引级别将从给定的level参数获取，并且输出为DataFrame**



| 参数： |
| ------ |

**①level：int，str，list，默认 -1**

​	**指定对哪个level上的列标签进行堆叠到行索引上**

**②dropna：bool，默认True**

​	**是否删除返回结果中的缺失值所在的行**

**③sort：bool，默认为True**

​	**是否对结果多索引的级别进行排序**

**④future_stack：bool，默认False**

​	**是否使用新的实现替换当前实现**



| 返回值： |
| -------- |

**:arrow_right:DataFrame或Series**





<img src="G:\01资料\Pictures\reshaping_stack.png" style="zoom:80%;" />





### DataFrame.unstack

**==DataFrame.unstack(*level=-1, fill_value=None, sort=True*)==**

​	**对分层的索引标签的某一级别进行透视，返回具有新级别的列标签的DataFrame，列标签的最内层由已透视的索引标签组成。如果索引不是多级索引，则输出将是一个Series**



| 参数： |
| ------ |

**①level：int，str，或 列表，默认 -1（最后一个层级）**

​	**指定unstack索引的层级,可以传递级别名称**

**②fill_value：int，str 或 字典**

​	**用于填充返回结果中的缺失值的值**

**③sort：bool，默认True**

​	**是否在结果中排序多级索引列的级别**



| 返回值： |
| -------- |

**:arrow_right:Series或DataFrame**



<img src="G:\01资料\Pictures\reshaping_unstack.png" style="zoom:80%;" />



<img src="G:\01资料\Pictures\reshaping_unstack_0.png" style="zoom:80%;" />



<img src="G:\01资料\Pictures\reshaping_unstack_1.png" style="zoom:80%;" />



### :a:列标签为单级索引

**对于如下的DataFrame**

```python
tuples = [
   ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
   ["one", "two", "one", "two", "one", "two", "one", "two"],
]
index = pd.MultiIndex.from_arrays(tuples, names=["first", "second"])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
print(df)

                     A         B
first second                    
bar   one    -0.443933 -0.906312
      two     0.353402 -1.929398
baz   one    -1.835238  0.062591
      two    -0.141351 -0.383688
foo   one     0.592539 -0.240536
      two    -1.171997 -0.477747
qux   one    -0.258457 -0.518656
      two    -0.967725 -0.976540
```



```python
stacked_df = df.stack()
print("=============对原DataFrame进行堆叠=============")
print(stacked_df)
print("============= 对已堆叠的对象进行逆堆叠，默认对最内层的索引进行操作=============")
unstack_df = stacked_df.unstack()
print(unstack_df)
print("============= 对已堆叠的对象进行逆堆叠，指定对第0层的的索引进行操作，level既可以是int，也可以是级别名=============")
print("=================stacked_df.unstack(0) 指定level = 0===============")
u1 = stacked_df.unstack(0)
print(u1)
print("=================stacked_df.unstack('first') 指定level = 'first'===============")
u11 = stacked_df.unstack('first')
print(u11)
print("============= 对已堆叠的对象进行逆堆叠，指定对第1层的的索引进行操作=============")
u2 = stacked_df.unstack(1)
print(u2)



#输出结果如下
=============对原DataFrame进行堆叠=============
first  second   
bar    one     A   -0.443933
               B   -0.906312
       two     A    0.353402
               B   -1.929398
baz    one     A   -1.835238
               B    0.062591
       two     A   -0.141351
               B   -0.383688
foo    one     A    0.592539
               B   -0.240536
       two     A   -1.171997
               B   -0.477747
qux    one     A   -0.258457
               B   -0.518656
       two     A   -0.967725
               B   -0.976540
dtype: float64
============= 对已堆叠的对象进行逆堆叠，默认对最内层的索引进行操作=============
                     A         B
first second                    
bar   one    -0.443933 -0.906312
      two     0.353402 -1.929398
baz   one    -1.835238  0.062591
      two    -0.141351 -0.383688
foo   one     0.592539 -0.240536
      two    -1.171997 -0.477747
qux   one    -0.258457 -0.518656
      two    -0.967725 -0.976540
============= 对已堆叠的对象进行逆堆叠，指定对第0层的的索引进行操作，level既可以是int，也可以是级别名=============
=================stacked_df.unstack(0) 指定level = 0===============
first          bar       baz       foo       qux
second                                          
one    A -0.443933 -1.835238  0.592539 -0.258457
       B -0.906312  0.062591 -0.240536 -0.518656
two    A  0.353402 -0.141351 -1.171997 -0.967725
       B -1.929398 -0.383688 -0.477747 -0.976540
=================stacked_df.unstack('first') 指定level = 'first'===============
first          bar       baz       foo       qux
second                                          
one    A -0.443933 -1.835238  0.592539 -0.258457
       B -0.906312  0.062591 -0.240536 -0.518656
two    A  0.353402 -0.141351 -1.171997 -0.967725
       B -1.929398 -0.383688 -0.477747 -0.976540
============= 对已堆叠的对象进行逆堆叠，指定对第1层的的索引进行操作=============
second        one       two
first                      
bar   A -0.443933  0.353402
      B -0.906312 -1.929398
baz   A -1.835238 -0.141351
      B  0.062591 -0.383688
foo   A  0.592539 -1.171997
      B -0.240536 -0.477747
qux   A -0.258457 -0.967725
      B -0.518656 -0.976540
```





### :b:列标签为多级索引

```python
columns = pd.MultiIndex.from_tuples(
    [
        ("A", "cat", "long"),
        ("B", "cat", "long"),
        ("A", "dog", "short"),
        ("B", "dog", "short"),
    ],
    names=["exp", "animal", "hair_length"],
)
df = pd.DataFrame(np.random.randn(4, 4), columns=columns)
print("==========原DataFrame===========")
print(df)
print("==========对df的列标签的 level=['animal', 'exp']这两个层级进行堆叠===========")
stacked_df = df.stack(level=['animal', 'exp'], future_stack=True)
print(stacked_df)
print("==========对df的列标签的 level=[1, 2] 即第二个和第三个级别进行堆叠===========")
stacked_df2 = df.stack(level=[1, 2], future_stack=True)
print(stacked_df2)



# 输出结果如下
==========原DataFrame===========
exp                 A         B         A         B
animal            cat       cat       dog       dog
hair_length      long      long     short     short
0           -0.330575  0.675064  0.473322 -0.648118
1           -1.343056  0.736805  0.457597  0.771460
2           -0.598720 -1.711055 -0.409595  0.041270
3            0.650673  0.304687 -1.472771  0.301760
==========对df的列标签的 level=['animal', 'exp']这两个层级进行堆叠===========
hair_length       long     short
  animal exp                    
0 cat    A   -0.330575       NaN
         B    0.675064       NaN
  dog    A         NaN  0.473322
         B         NaN -0.648118
1 cat    A   -1.343056       NaN
         B    0.736805       NaN
  dog    A         NaN  0.457597
         B         NaN  0.771460
2 cat    A   -0.598720       NaN
         B   -1.711055       NaN
  dog    A         NaN -0.409595
         B         NaN  0.041270
3 cat    A    0.650673       NaN
         B    0.304687       NaN
  dog    A         NaN -1.472771
         B         NaN  0.301760
==========对df的列标签的 level=[1, 2] 即第二个和第三个级别进行堆叠===========
exp                          A         B
  animal hair_length                    
0 cat    long        -0.330575  0.675064
  dog    short        0.473322 -0.648118
1 cat    long        -1.343056  0.736805
  dog    short        0.457597  0.771460
2 cat    long        -0.598720 -1.711055
  dog    short       -0.409595  0.041270
3 cat    long         0.650673  0.304687
  dog    short       -1.472771  0.301760

```





## 3、`melt()` 和 `wide_to_long()`

<img src="G:\01资料\Pictures\reshaping_melt.png" style="zoom:80%;" />



### pandas.melt

**==pandas.melt(*frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True*)==**

​	**将DataFrame从宽格式转换为长格式，可选择保留标识符位置**

​	**此函数可用于将DataFrame调整为一种格式，其中一个或多个列是标识符变量（*id_vars*），而所有其他列（被视为观测变量（*value_vars*））都不旋转到行轴，只留下两个非标识符列，变量（*variable*） 和 值（*value*）**



| 参数： |
| ------ |

**①frame：DataFrame**

**②id_vars：标量，元组，列表，ndarray，可选**

​	**用于作为指示变量的列**

**③value_vars：标量，元组，列 或 ndarray，可选**

​	**要逆透视的列，如果未指定，则使用所有未设置为*id_vars*的列**

**④var_name：标量，默认None**

​	**用于 'variable' 列的名称，如果为None，则使用`frame.columns.name` 或 'variable'**

**⑤value_name：标量，默认'value'**

​	**用于 'value' 列的名称，不能是现有的列标签**

**⑥col_level：标量，可选**

​	**如果列是多级索引，则使用此级别进行融化**

**⑦ignore_index：bool，默认True**

​	**是否忽略原索引**



| 返回值： |
| -------- |

**:arrow_right:返回逆透视的DataFrame**





```python
cheese = pd.DataFrame(
    {
        "first": ["John", "Mary"],
        "last": ["Doe", "Bo"],
        "height": [5.5, 6.0],
        "weight": [130, 150],
        "A": [2, 3]
    }
)
print("==========原DataFrame===========")
print(cheese)
print("==========将 ['first', 'last'] 设置为标识符变量的列，即结果中的行索引===========")
print(cheese.melt(id_vars=['first', 'last']))
print("==========将 ['first', 'last'] 设置为标识符变量的列，指定只对A列进行逆透视===========")
print(cheese.melt(id_vars=['first', 'last'], value_vars='A'))
print("==========将 ['first', 'last'] 设置为标识符变量的列，默认对所有列进行逆透视，并指定'variable'和'value'两列的名称===========")
print(cheese.melt(id_vars=['first', 'last'], var_name='quantity', value_name='show'))



#输出结果如下
==========原DataFrame===========
  first last  height  weight  A
0  John  Doe     5.5     130  2
1  Mary   Bo     6.0     150  3
==========将 ['first', 'last'] 设置为标识符变量的列，即结果中的行索引===========
  first last variable  value
0  John  Doe   height    5.5
1  Mary   Bo   height    6.0
2  John  Doe   weight  130.0
3  Mary   Bo   weight  150.0
4  John  Doe        A    2.0
5  Mary   Bo        A    3.0
==========将 ['first', 'last'] 设置为标识符变量的列，指定只对A列进行逆透视===========
  first last variable  value
0  John  Doe        A      2
1  Mary   Bo        A      3
==========将 ['first', 'last'] 设置为标识符变量的列，默认对所有列进行逆透视，并指定'variable'和'value'两列的名称===========
  first last quantity   show
0  John  Doe   height    5.5
1  Mary   Bo   height    6.0
2  John  Doe   weight  130.0
3  Mary   Bo   weight  150.0
4  John  Doe        A    2.0
5  Mary   Bo        A    3.0
```





### pandas.wide_to_long

**==pandas.wide_to_long(*df, stubnames, i, j, sep='', suffix='\\d+'*)==**

​	**将DataFrame从宽格式转成长格式，相较于`melt()`来说，灵活性较差，但更加用户友好**

​	**使用stunames['A', 'B']，此函数希望找到一组或多组格式为A-suffix1、A-suffix2、...、B-suffix1、B-suffix2、...的列，可以使用`j`在结果的长格式中指定后缀名**



| 参数： |
| ------ |

**①df：DataFrame**

​	**宽格式的DataFrame**

**②stubnames：str 或 列表**

​	**存根名称，宽格式变量假定以存根名称开头**

**③i：字符串 或 列表**

​	**用作id变量的列**

**④j：str**

​	**子观察变量的名称，长格式后缀名**

**⑤sep：str，默认""**

​	**用于指示宽格式中变量名称的分隔符**

**⑥suffix：str，默认'\\d+'**

​	**一个用于捕获所需后缀的正则表达式**



| 返回值： |
| -------- |

**:arrow_right:返回包含每个存根名称作为变量的DataFrame，具有新索引`(i, j)`**



**`wide_to_long()`方法适合多风格的列名**

```python
In [56]: dft = pd.DataFrame(
   ....:     {
   ....:         "A1970": {0: "a", 1: "b", 2: "c"},
   ....:         "A1980": {0: "d", 1: "e", 2: "f"},
   ....:         "B1970": {0: 2.5, 1: 1.2, 2: 0.7},
   ....:         "B1980": {0: 3.2, 1: 1.3, 2: 0.1},
   ....:         "X": dict(zip(range(3), np.random.randn(3))),
   ....:     }
   ....: )
   ....: 

In [57]: dft["id"] = dft.index

In [58]: dft
Out[58]: 
  A1970 A1980  B1970  B1980         X  id
0     a     d    2.5    3.2  1.519970   0
1     b     e    1.2    1.3 -0.493662   1
2     c     f    0.7    0.1  0.600178   2

In [59]: pd.wide_to_long(dft, ["A", "B"], i="id", j="year")
Out[59]: 
                X  A    B
id year                  
0  1970  1.519970  a  2.5
1  1970 -0.493662  b  1.2
2  1970  0.600178  c  0.7
0  1980  1.519970  d  3.2
1  1980 -0.493662  e  1.3
2  1980  0.600178  f  0.1



----------------------------------------------------------------------------------------------------
>>> df = pd.DataFrame({
...     'famid': [1, 1, 1, 2, 2, 2, 3, 3, 3],
...     'birth': [1, 2, 3, 1, 2, 3, 1, 2, 3],
...     'ht_one': [2.8, 2.9, 2.2, 2, 1.8, 1.9, 2.2, 2.3, 2.1],
...     'ht_two': [3.4, 3.8, 2.9, 3.2, 2.8, 2.4, 3.3, 3.4, 2.9]
... })
>>> df
   famid  birth  ht_one  ht_two
0      1      1     2.8     3.4
1      1      2     2.9     3.8
2      1      3     2.2     2.9
3      2      1     2.0     3.2
4      2      2     1.8     2.8
5      2      3     1.9     2.4
6      3      1     2.2     3.3
7      3      2     2.3     3.4
8      3      3     2.1     2.9


>>> l = pd.wide_to_long(df, stubnames='ht', i=['famid', 'birth'], j='age',
...                     sep='_', suffix=r'\w+')
>>> l
... 
                  ht
famid birth age
1     1     one  2.8
            two  3.4
      2     one  2.9
            two  3.8
      3     one  2.2
            two  2.9
2     1     one  2.0
            two  3.2
      2     one  1.8
            two  2.8
      3     one  1.9
            two  2.4
3     1     one  2.2
            two  3.3
      2     one  2.3
            two  3.4
      3     one  2.1
            two  2.9
```







## 4、`explode()`

​		**此例程将分解类列表数据，包括列表、元组、集合、系列和ndarray，标量将保持不变，空列表类将导致该行返回np.nan，分解集合时，输出元素顺序不确定，其他情况下，输出均为 *object*对象**



### Series.explode

**==Series.explode(*ignore_index=False*)==**

​	**把每一行的列表类元素摊开**

​	**ignore_index表示是否忽略索引，如果忽略，则索引标签将为0,1,...n-1**



**:arrow_right:返回Series，Series中的元素为已经扩张的每行的列表，索引为原Series中这些行索引的重复**



```python
s = pd.Series([[1, 2, 3], 'foo', [], [3, 4]], index=list('abcd'))
print("============原Series===============")
print(s)
print("============s.explode()================")
print(s.explode())
print("============s.explode(ignore_index=True) 忽略原索引================")
print(s.explode(ignore_index=True))



#输出结果如下
============原Series===============
a    [1, 2, 3]
b          foo
c           []
d       [3, 4]
dtype: object
============s.explode()================
a      1
a      2
a      3
b    foo
c    NaN
d      3
d      4
dtype: object
============s.explode(ignore_index=True) 忽略原索引================
0      1
1      2
2      3
3    foo
4    NaN
5      3
6      4
dtype: object
```



### DataFrame.explode

**==DataFrame.explode(*column, ignore_index=False*)==**

​	**将某一列的列表类的值摊开**

​	***column*需指定索引标签，表示对哪一列或哪些列的列表类的值摊开**



**:arrow_right:DataFrame，其索引会重复**



```python
df = pd.DataFrame({'A': [[0, 1, 2], 'foo', [], [3, 4]],
                   'B': 1,
                   'C': [['a', 'b', 'c'], np.nan, [], ['d', 'e']]},
                  index = list('abcd'))
print("================原DataFrame====================")
print(df)
print("===============df.explode('A') 只对A列的列表类数据摊开 ===================")
print(df.explode('A'))
print("===============df.explode(['A', 'C']) 对A、C两列列的列表类数据摊开 ===================")
print(df.explode(['A', 'C']))



# 输出结果如下
================原DataFrame====================
           A  B          C
a  [0, 1, 2]  1  [a, b, c]
b        foo  1        NaN
c         []  1         []
d     [3, 4]  1     [d, e]
===============df.explode('A') 只对A列的列表类数据摊开 ===================
     A  B          C
a    0  1  [a, b, c]
a    1  1  [a, b, c]
a    2  1  [a, b, c]
b  foo  1        NaN
c  NaN  1         []
d    3  1     [d, e]
d    4  1     [d, e]
===============df.explode(['A', 'C']) 对A、C两列列的列表类数据摊开 ===================
     A  B    C
a    0  1    a
a    1  1    b
a    2  1    c
b  foo  1  NaN
c  NaN  1  NaN
d    3  1    d
d    4  1    e
```



**一个特别的例子， 其中`assign()`的作用是对原先的DataFrame多加一列，或者改变某列的值**

```python
df = pd.DataFrame([{"var1": "a,b,c", "var2": 1}, {"var1": "d,e,f", "var2": 2}])
print("==============原DataFrame================")
print(df)
print("================对原DataFrame的var1列的值转换为列表，使用str访问器实现======================")
new_df = df.assign(var1=df['var1'].str.split(','))
print(new_df)
print("=================只对var1列中的列表类进行摊开==========================")
print(new_df.explode('var1'))


# 输出结果如下
==============原DataFrame================
    var1  var2
0  a,b,c     1
1  d,e,f     2
================对原DataFrame的var1列的值转换为列表，使用str访问器实现======================
        var1  var2
0  [a, b, c]     1
1  [d, e, f]     2
=================只对var1列中的列表类进行摊开==========================
  var1  var2
0    a     1
0    b     1
0    c     1
1    d     2
1    e     2
1    f     2
```







## 5、`factorize()`

### pandas.factorize

**==pandas.factorize(*values, sort=False, use_na_sentinel=True, size_hint=None*)==**

​	**将对象编码为枚举类型或分类变量，类似的方法有`Series.factorize()`和`Index.factorize()`**



| 参数： |
| ------ |

**①values：序列**

​	**一维序列，非pandas对象在序列分解之前会被强制转换为ndarray**

**②sort：bool，默认True**

​	**是否对唯一值进行排序**

**③use_na_sentinel：bool，默认True**

​	**如果为True，则NaN值将被标记为-1，如果为False，则NaN值将被编码为非负整数，并且不会从values中的唯一值中删除NaN**

**④size_hint：int，可选**

​	**预先分配哈希表的大小**



| 返回值： |
| -------- |

**:arrow_right:codes：ndarray**

​	**用于重建数据的索引的ndarray**

**:arrow_right:uniques：ndarray，Index，或 Categorical**

​	**唯一值的序列。当values为Categorical时，返回Categorical；当values为其他Pandas对象是，返回Index；否则，返回一维ndarray**



```python
print("=================values = ndarray==========================")
print("=================唯一值数组的顺序 按出现顺序==========================")
codes, uniques = pd.factorize(np.array(['b', None, 'a', 'c', 'b'], dtype="O"))
print(f"重建原数据的编码  --》 {codes}")
print(f"唯一值序列 --》 {uniques}")
print("=================指定对唯一值数组的元素进行排序==========================")
codes, uniques = pd.factorize(np.array(['b', None, 'a', 'c', 'b'], dtype="O"), sort=True)
print(f"重建原数据的编码  --》 {codes}")
print(f"唯一值序列 --》 {uniques}")
print("=========对于缺失值的标记值，传入use_na_sentinel=False，即不使用默认的-1进行标记=============")
codes, uniques = pd.factorize(np.array(['b', None, 'a', 'c', 'b'], dtype="O"), use_na_sentinel=False)
print(f"重建原数据的编码  --》 {codes}")
print(f"唯一值序列 --》 {uniques}")
print("=================values = Series==========================")
codes, uniques = pd.factorize(pd.Series(['a', 'c', 'c', 'b']))
print(f"重建原数据的编码  --》 {codes}")
print(f"唯一值序列 --》 {uniques}")
print("=================values = Categorical==========================")
cat = pd.Categorical(['a', 'a', 'c', 'd'], categories=['a', 'b', 'c'])
codes, uniques = pd.factorize(cat)
print(f"重建原数据的编码  --》 {codes}")
print(f"唯一值序列 --》 {uniques}")



#输出结果如下
=================values = ndarray==========================
=================唯一值数组的顺序 按出现顺序==========================
重建原数据的编码  --》 [ 0 -1  1  2  0]
唯一值序列 --》 ['b' 'a' 'c']
=================指定对唯一值数组的元素进行排序==========================
重建原数据的编码  --》 [ 1 -1  0  2  1]
唯一值序列 --》 ['a' 'b' 'c']
=========对于缺失值的标记值，传入use_na_sentinel=False，即不使用默认的-1进行标记=============
重建原数据的编码  --》 [0 1 2 3 0]
唯一值序列 --》 ['b' nan 'a' 'c']
=================values = Series==========================
重建原数据的编码  --》 [0 1 1 2]
唯一值序列 --》 Index(['a', 'c', 'b'], dtype='object')
=================values = Categorical==========================
重建原数据的编码  --》 [ 0  0  1 -1]
唯一值序列 --》 ['a', 'c']
Categories (3, object): ['a', 'b', 'c']
```







# 十、合并、连接、串联和比较

**Pandas提供了多种组合和比较Series或DataFrame的方法**

- **`concat()`：沿着共享的索引或列拼接多个Series或DataFrame对象**
- **`DataFrame.join()`：沿着列合并多个DataFrame对象**
- **`DataFrame.combine_first()`：在两个DataFrame的相同位置，使用非缺失值替换缺失值**
- **`merge()`：使用SQL风格的连接来组合两个Series或DataFrame**
- **`merge_ordered()`：沿着有序的轴合并两个Series或DataFrame**
- **`merge_asof()`：近似匹配，使用接近的而不是精确匹配的键来合并两个Series或DataFrame**
- **`Series.compare()`和`DataFrame.compare()`：显示两个Series或DataFrame对象的不同的values**



 

## pandas.concat

**==pandas.concat(*objs, axis=0, join='outer', ignore_index=False, keys=None, levels=None, name=None, verify_integrity=False, sort=False, copy=None*)==**

​	**沿着特定的轴拼接多个DataFrame**



| 参数： |
| ------ |

**①objs：一个序列，或Series的映射 或 DataFrame**

​	**如果传递了映射关系，则已排序的键将用作 *keys* 参数，任何None的对象均会被丢弃**

**②axis：{0或'index'，1 或 'columns'}，默认0**

​	**沿哪个轴连接**

**③join：{'inner', 'outer'}，默认'outer'**

​	**`join='inner'`，取所有轴标签的交集，`join='outer'`取所有轴标签的并集，默认是`outer`**

**④ignore_index：bool，默认False**

​	**是否忽略原索引**

**⑤keys：序列，默认None**

​	**如果传递了多个层级，则应该使用元组。使用传递的键作为最外层来构建分级索引**

**⑥level：序列列表，默认None**

​	**用于构建多级索引的特定层级**

**⑦names：列表，默认None**

​	**生成的层次索引中各级别的名称**

**⑧sort：bool，默认False**

​	**是否进行排序**

**⑨copy：bool，默认True**

​	**是否复制数据**



| 返回值： |
| -------- |

**:arrow_right:Series或DataFrame**



### :a:Series和DataFrame做拼接

```python
s1 = pd.Series(["X0", "X1", "X2", "X3"], name="X")
s2 = pd.Series(["X0", "X1", "X2", "X3"], index=["A", "B", "C", "D"])
df = pd.DataFrame(
     {
         "A": ["A0", "A1", "A2", "A3"],
         "B": ["B0", "B1", "B2", "B3"],
         "C": ["C0", "C1", "C2", "C3"],
         "D": ["D0", "D1", "D2", "D3"],
     },
     index=[0, 1, 2, 3],
 )
print("=============原Series1==================")
print(s1)
print("=============原Series2==================")
print(s2)
print("=============原DataFrame==================")
print(df)
print("=============把Series1拼接到DataFrame的最后一列的后面==================")
print(pd.concat([df1, s1], axis='columns'))
print("=============把Series2拼接到DataFrame的最后一行的后面,因为Series是一列，所以使用 s2.to_frame().T 把它转成一行==================")
print(pd.concat([df1, s2.to_frame().T]))



#输出结果如下
=============原Series1==================
0    X0
1    X1
2    X2
3    X3
Name: X, dtype: object
=============原Series2==================
A    X0
B    X1
C    X2
D    X3
dtype: object
=============原DataFrame==================
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
=============把Series1拼接到DataFrame的最后一列的后面==================
    A   B   C   D   X
0  A0  B0  C0  D0  X0
1  A1  B1  C1  D1  X1
2  A2  B2  C2  D2  X2
3  A3  B3  C3  D3  X3
=============把Series2拼接到DataFrame的最后一行的后面,因为Series是一列，所以使用 s2.to_frame().T 把它转成一行==================
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
0  X0  X1  X2  X3
```





### :b:两个DataFrame做拼接

```python
df1 = pd.DataFrame(
     {
         "A": ["A0", "A1", "A2", "A3"],
         "B": ["B0", "B1", "B2", "B3"],
         "C": ["C0", "C1", "C2", "C3"],
         "D": ["D0", "D1", "D2", "D3"],
     },
     index=[0, 1, 2, 3],
 )

df2 = pd.DataFrame(
     {
         "A": ["A4", "A5", "A6", "A7"],
         "B": ["B4", "B5", "B6", "B7"],
         "C": ["C4", "C5", "C6", "C7"],
         "D": ["D4", "D5", "D6", "D7"],
     },
     index=[4, 5, 6, 7],
 )

df3 = pd.DataFrame(
     {
         "A": ["A8", "A9", "A10", "A11"],
         "B": ["B8", "B9", "B10", "B11"],
         "C": ["C8", "C9", "C10", "C11"],
         "D": ["D8", "D9", "D10", "D11"],
     },
     index=[8, 9, 10, 11],
 )
df4 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7],
)
print("===============原表1=================")
print(df1)
print("===============原表2=================")
print(df2)
print("===============原表3=================")
print(df3)
print("===============原表4=================")
print(df4)
print("=============== 拼接表1 2 3后， 默认对行做拼接，默认对所有轴标签取并集=================")
print(pd.concat([df1, df2, df3]))
print("=============== 拼接表1 2 3后， 默认对行做拼接，默认对所有轴标签取并集，指定keys关键字来沿着拼接轴指定最外层索引=================")
print(pd.concat([df1, df2, df3], keys=['x', 'y', 'z']))
print("=============== 拼接表1 2 3，第一个参数也可以是字典，键是keys参数，值是拼接的对象，等价于上面的调用=================")
pieces = {"x": df1, "y": df2, "z": df3}
print(pd.concat(pieces))
print("=============== 拼接表1和表4后， 指定对列做拼接， 默认对所有轴标签取并集=================")
print(pd.concat([df1, df4], axis='columns'))
print("=============== 拼接表1和表4后， 指定对列做拼接, 指定对所有轴标签取交集=================")
print(pd.concat([df1, df4], axis='columns', join='inner'))
print("=============== 拼接表1和表4后， 指定沿对列作拼接, 忽略原先索引=================")
print(pd.concat([df1, df4], axis='columns', ignore_index=True))



# 输出结果如下
===============原表1=================
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
===============原表2=================
    A   B   C   D
4  A4  B4  C4  D4
5  A5  B5  C5  D5
6  A6  B6  C6  D6
7  A7  B7  C7  D7
===============原表3=================
      A    B    C    D
8    A8   B8   C8   D8
9    A9   B9   C9   D9
10  A10  B10  C10  D10
11  A11  B11  C11  D11
===============原表4=================
    B   D   F
2  B2  D2  F2
3  B3  D3  F3
6  B6  D6  F6
7  B7  D7  F7
=============== 拼接表1 2 3后， 默认对行做拼接，默认对所有轴标签取并集=================
      A    B    C    D
0    A0   B0   C0   D0
1    A1   B1   C1   D1
2    A2   B2   C2   D2
3    A3   B3   C3   D3
4    A4   B4   C4   D4
5    A5   B5   C5   D5
6    A6   B6   C6   D6
7    A7   B7   C7   D7
8    A8   B8   C8   D8
9    A9   B9   C9   D9
10  A10  B10  C10  D10
11  A11  B11  C11  D11
=============== 拼接表1 2 3后， 默认对行做拼接，默认对所有轴标签取并集，指定keys关键字来沿着拼接轴指定最外层索引=================
        A    B    C    D
x 0    A0   B0   C0   D0
  1    A1   B1   C1   D1
  2    A2   B2   C2   D2
  3    A3   B3   C3   D3
y 4    A4   B4   C4   D4
  5    A5   B5   C5   D5
  6    A6   B6   C6   D6
  7    A7   B7   C7   D7
z 8    A8   B8   C8   D8
  9    A9   B9   C9   D9
  10  A10  B10  C10  D10
  11  A11  B11  C11  D11
=============== 拼接表1 2 3，第一个参数也可以是字典，键是keys参数，值是拼接的对象，等价于上面的调用=================
        A    B    C    D
x 0    A0   B0   C0   D0
  1    A1   B1   C1   D1
  2    A2   B2   C2   D2
  3    A3   B3   C3   D3
y 4    A4   B4   C4   D4
  5    A5   B5   C5   D5
  6    A6   B6   C6   D6
  7    A7   B7   C7   D7
z 8    A8   B8   C8   D8
  9    A9   B9   C9   D9
  10  A10  B10  C10  D10
  11  A11  B11  C11  D11
=============== 拼接表1和表4后， 指定对列做拼接， 默认对所有轴标签取并集=================
     A    B    C    D    B    D    F
0   A0   B0   C0   D0  NaN  NaN  NaN
1   A1   B1   C1   D1  NaN  NaN  NaN
2   A2   B2   C2   D2   B2   D2   F2
3   A3   B3   C3   D3   B3   D3   F3
6  NaN  NaN  NaN  NaN   B6   D6   F6
7  NaN  NaN  NaN  NaN   B7   D7   F7
=============== 拼接表1和表4后， 指定对列做拼接, 指定对所有轴标签取交集=================
    A   B   C   D   B   D   F
2  A2  B2  C2  D2  B2  D2  F2
3  A3  B3  C3  D3  B3  D3  F3
=============== 拼接表1和表4后， 指定沿对列作拼接, 忽略原先索引=================
     0    1    2    3    4    5    6
0   A0   B0   C0   D0  NaN  NaN  NaN
1   A1   B1   C1   D1  NaN  NaN  NaN
2   A2   B2   C2   D2   B2   D2   F2
3   A3   B3   C3   D3   B3   D3   F3
6  NaN  NaN  NaN  NaN   B6   D6   F6
7  NaN  NaN  NaN  NaN   B7   D7   F7
```





**下面两个函数实现了表连接**

<img src="G:\01资料\Pictures\SQL_join.png" style="zoom:50%;" />





## pandas.merge

**==pandas.merge(*left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=None, indicator=False, validate=None*)==**

​	**连接两个DataFrame或Series**



| 参数： |
| ------ |

**①left/right：DataFrame 或 命名Series**

​	**要连接的左/右表**

**②how：{'left', 'right', 'outer', 'inner', 'cross'}，默认'inner'**

​	**表的连接方式，依次为左外连接（left join），右外连接(right join)，内连接(inner join)，全外连接(full join)和笛卡尔积连接**

| 连接方法 | SQL 连接名         | 描述                               |
| -------- | ------------------ | ---------------------------------- |
| `left`   | `LEFT OUTER JOIN`  | Use keys from left frame only      |
| `right`  | `RIGHT OUTER JOIN` | Use keys from right frame only     |
| `outer`  | `FULL OUTER JOIN`  | Use union of keys from both frames |
| `inner`  | `INNER JOIN`       | 使用两个DataFrame键的交集          |
| `cross`  | `CROSS JOIN`       | 笛卡尔积连接                       |

**③on：标签 或 列表**

​	**表连接条件**

**④left_on/right_on：标签或列表或数组**

​	**左表/右表连接条件**

**⑤left_index/right_index：bool，默认False**

​	**使用左侧/右侧DataFrame的索引作为连接键**

**⑥sort：bool，默认False**

​	**是否对连接条件的键进行排序**

**⑦suffixes：列表，默认为("_x", "\_y")**

​	**长度为2的序列，每个元素表示分别添加到左侧和右侧重复列名的后缀上**

**⑧copy：bool，默认True**

​	**是否复制数据**

**⑨indicator：bool或str，默认False**

​	**如果为True，则在返回结果中添加一个名为'_merge'的列，显示每行的数据源，该列为分类类型，其值为**

- **left_only：只来自左表**
- **right_only：只来自右表**
- **both：两表中都有**

**⑩validate：str，可选**

​	**验证表连接类型，是一对一、一对多、多对一还是多对多**





### :a:指定`on`参数

```python
left = pd.DataFrame({"k": ["K0", "K1", "K2"], "v1": [1, 2, 3]})
right = pd.DataFrame({"k": ["K0", "K0", "K3"], "v2": [4, 5, 6]})
print("=============原DataFrame1==================")
print(left)
print("=============原DataFrame2==================")
print(left)
print("=============连接两个DataFrame,指定连接的键为 k,即 on = 'k' ,指定后缀('_l', '_r')，后缀只有两个表有相同列名时才发挥作用==================")
print(pd.merge(left, right, on="k", suffixes=('_l', '_r')))



# 输出结果如下
=============原DataFrame1==================
    k  v1
0  K0   1
1  K1   2
2  K2   3
=============原DataFrame2==================
    k  v1
0  K0   1
1  K1   2
2  K2   3
=============连接两个DataFrame,指定连接的键为 k,即 on = 'k' ,指定后缀('_l', '_r')，后缀只有两个表有相同列名时才发挥作用==================
    k  v1  v2
0  K0   1   4
1  K0   1   5
```



```python
df3 = pd.DataFrame({"lkey": ["b", "b", "a", "c", "a","a","b"], "data": pd.Series(range(7), dtype="Int64")})
df4 = pd.DataFrame({"rkey": ["a", "b", "d"], "data": pd.Series(range(3), dtype="Int64")})
print("=============原DataFrame1==================")
print(df3)
print("=============原DataFrame2==================")
print(df4)
print("=============连接两个DataFrame, 连接左表的键为lkey，连接右表的键为rkey，指定后缀('_l', '_r')==================")
print(pd.merge(df3, df4, left_on='lkey', right_on='rkey', suffixes=('_l', '_r')))



# 输出结果如下
=============原DataFrame1==================
  lkey  data
0    b     0
1    b     1
2    a     2
3    c     3
4    a     4
5    a     5
6    b     6
=============原DataFrame2==================
  rkey  data
0    a     0
1    b     1
2    d     2
=============连接两个DataFrame, 连接左表的键为lkey，连接右表的键为rkey，指定后缀('_l', '_r')==================
  lkey  data_l rkey  data_r
0    b       0    b       1
1    b       1    b       1
2    a       2    a       0
3    a       4    a       0
4    a       5    a       0
5    b       6    b       1

```





### :b:不指定`on`参数

​	**由于两表中的键相同，所以可以不指定`on`参数，这时pandas把相同列标签当作连接条件**

```python
import random

# 生成客户表
customer_ids = list(range(1001, 1011))  # 10 customers
names = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

customers = pd.DataFrame({
    'customer_id': customer_ids,
    'name': names,
    'city': [random.choice(cities) for _ in range(10)]
})

# 生成订单表
orders = []
for i in range(1, 9):  # 20 orders
    customer_id = random.choice(customer_ids + [1011, 1012])  # Add some unknown customer_ids
    product = random.choice(['Laptop', 'Book', 'Phone', 'T-Shirt', 'Backpack'])
    price = random.choice([1200, 30, 500, 25, 60])
    orders.append([i, customer_id, product, price])

orders = pd.DataFrame(orders, columns=['order_id', 'customer_id', 'product', 'price'])

print("==============顾客表===============")
print(customers)
print("==============订单表===============")
print(orders)
print("===========连接顾客表和订单表，默认内连接，由于两个表中有相同的列，所以可推断=============")
print(pd.merge(customers, orders))
print("===========连接顾客表和订单表，左外连接=============")
print(pd.merge(customers, orders, how='left'))
print("===========连接顾客表和订单表，右外连接=============")
print(pd.merge(customers, orders, how='right'))
print("===========连接顾客表和订单表，全外连接=============")
print(pd.merge(customers, orders, how='outer'))
print("===========连接顾客表和订单表，笛卡尔积连接,指定显示前五行=============")
print(pd.merge(customers, orders, how='cross').head())
print("===========连接顾客表和订单表，默认内连接，显示每行的数据源=============")
print(pd.merge(customers, orders, how='outer', indicator=True))



# 输出结果如下
==============顾客表===============
   customer_id   name         city
0         1001  Alice     New York
1         1002    Bob      Chicago
2         1003  Carol     New York
3         1004   Dave      Houston
4         1005    Eve      Phoenix
5         1006  Frank  Los Angeles
6         1007  Grace     New York
7         1008  Heidi      Houston
8         1009   Ivan      Houston
9         1010   Judy      Phoenix
==============订单表===============
   order_id  customer_id   product  price
0         1         1012  Backpack   1200
1         2         1003      Book     25
2         3         1011      Book     25
3         4         1011     Phone   1200
4         5         1001    Laptop   1200
5         6         1011  Backpack   1200
6         7         1012      Book     30
7         8         1005    Laptop   1200
===========连接顾客表和订单表，默认内连接，由于两个表中有相同的列，所以可推断=============
   customer_id   name      city  order_id product  price
0         1001  Alice  New York         5  Laptop   1200
1         1003  Carol  New York         2    Book     25
2         1005    Eve   Phoenix         8  Laptop   1200
===========连接顾客表和订单表，左外连接=============
   customer_id   name         city  order_id product   price
0         1001  Alice     New York       5.0  Laptop  1200.0
1         1002    Bob      Chicago       NaN     NaN     NaN
2         1003  Carol     New York       2.0    Book    25.0
3         1004   Dave      Houston       NaN     NaN     NaN
4         1005    Eve      Phoenix       8.0  Laptop  1200.0
5         1006  Frank  Los Angeles       NaN     NaN     NaN
6         1007  Grace     New York       NaN     NaN     NaN
7         1008  Heidi      Houston       NaN     NaN     NaN
8         1009   Ivan      Houston       NaN     NaN     NaN
9         1010   Judy      Phoenix       NaN     NaN     NaN
===========连接顾客表和订单表，右外连接=============
   customer_id   name      city  order_id   product  price
0         1012    NaN       NaN         1  Backpack   1200
1         1003  Carol  New York         2      Book     25
2         1011    NaN       NaN         3      Book     25
3         1011    NaN       NaN         4     Phone   1200
4         1001  Alice  New York         5    Laptop   1200
5         1011    NaN       NaN         6  Backpack   1200
6         1012    NaN       NaN         7      Book     30
7         1005    Eve   Phoenix         8    Laptop   1200
===========连接顾客表和订单表，全外连接=============
    customer_id   name         city  order_id   product   price
0          1001  Alice     New York       5.0    Laptop  1200.0
1          1002    Bob      Chicago       NaN       NaN     NaN
2          1003  Carol     New York       2.0      Book    25.0
3          1004   Dave      Houston       NaN       NaN     NaN
4          1005    Eve      Phoenix       8.0    Laptop  1200.0
5          1006  Frank  Los Angeles       NaN       NaN     NaN
6          1007  Grace     New York       NaN       NaN     NaN
7          1008  Heidi      Houston       NaN       NaN     NaN
8          1009   Ivan      Houston       NaN       NaN     NaN
9          1010   Judy      Phoenix       NaN       NaN     NaN
10         1011    NaN          NaN       3.0      Book    25.0
11         1011    NaN          NaN       4.0     Phone  1200.0
12         1011    NaN          NaN       6.0  Backpack  1200.0
13         1012    NaN          NaN       1.0  Backpack  1200.0
14         1012    NaN          NaN       7.0      Book    30.0
===========连接顾客表和订单表，笛卡尔积连接,指定显示前五行=============
   customer_id_x   name      city  order_id  customer_id_y   product  price
0           1001  Alice  New York         1           1012  Backpack   1200
1           1001  Alice  New York         2           1003      Book     25
2           1001  Alice  New York         3           1011      Book     25
3           1001  Alice  New York         4           1011     Phone   1200
4           1001  Alice  New York         5           1001    Laptop   1200
===========连接顾客表和订单表，默认内连接，显示每行的数据源=============
    customer_id   name         city  order_id   product   price      _merge
0          1001  Alice     New York       5.0    Laptop  1200.0        both
1          1002    Bob      Chicago       NaN       NaN     NaN   left_only
2          1003  Carol     New York       2.0      Book    25.0        both
3          1004   Dave      Houston       NaN       NaN     NaN   left_only
4          1005    Eve      Phoenix       8.0    Laptop  1200.0        both
5          1006  Frank  Los Angeles       NaN       NaN     NaN   left_only
6          1007  Grace     New York       NaN       NaN     NaN   left_only
7          1008  Heidi      Houston       NaN       NaN     NaN   left_only
8          1009   Ivan      Houston       NaN       NaN     NaN   left_only
9          1010   Judy      Phoenix       NaN       NaN     NaN   left_only
10         1011    NaN          NaN       3.0      Book    25.0  right_only
11         1011    NaN          NaN       4.0     Phone  1200.0  right_only
12         1011    NaN          NaN       6.0  Backpack  1200.0  right_only
13         1012    NaN          NaN       1.0  Backpack  1200.0  right_only
14         1012    NaN          NaN       7.0      Book    30.0  right_only
```







## DataFrame.join

**==DataFrame.join(*other, on=None, how='left', lsuffix='', rsuffix='', sort=False, validate=None*)==**

​	**表连接，pandas中体现为两个DataFrame连接**



| 参数： |
| ------ |

**①other：DataFrame，Series**

​	**要连接的表**

**②on：str，str的列表，类数组，可选**

​	**表连接条件，如果为None，则自动推断**

**③how：{'left', 'right', 'outer', 'inner', 'cross'}，默认'left'**

​	**表连接方式，依次为左连接，右连接，外连接，内连接以及笛卡尔积连接**

**④lsuffix/rsuffix：str，默认**

​	**左/右表重复列的后缀**

**⑤sort：bool，默认False**

​	**是否排序**

**⑥validate：{'1:1', '1:m', 'm:1', 'm:m'}，可选**

​	**用于检查表的连接方式是 一对一、一对多、多对一还是多对多**



| 返回值： |
| -------- |

**:arrow_right:DataFrame**



```python
In [91]: left = pd.DataFrame(
   ....:     {
   ....:         "A": ["A0", "A1", "A2", "A3"],
   ....:         "B": ["B0", "B1", "B2", "B3"],
   ....:         "key": ["K0", "K1", "K0", "K1"],
   ....:     }
   ....: )
   ....: 

In [92]: right = pd.DataFrame({"C": ["C0", "C1"], "D": ["D0", "D1"]}, index=["K0", "K1"])

In [93]: result = left.join(right, on="key")

In [94]: result
Out[94]: 
    A   B key   C   D
0  A0  B0  K0  C0  D0
1  A1  B1  K1  C1  D1
2  A2  B2  K0  C0  D0
3  A3  B3  K1  C1  D1
```







## pandas.merge_asof

**近似匹配，类似于表的左连接，其中tolerance参数可以指定近似程度，若`tolerance=n`，则匹配的范围是 右表 $-$左表 $\le $ n**

### :a:实例

```python
quotes = pd.DataFrame(
    {
        "time": [
            pd.Timestamp("2016-05-25 13:30:00.023"),
            pd.Timestamp("2016-05-25 13:30:00.023"),
            pd.Timestamp("2016-05-25 13:30:00.030"),
            pd.Timestamp("2016-05-25 13:30:00.041"),
            pd.Timestamp("2016-05-25 13:30:00.048"),
            pd.Timestamp("2016-05-25 13:30:00.049"),
            pd.Timestamp("2016-05-25 13:30:00.072"),
            pd.Timestamp("2016-05-25 13:30:00.075")
        ],
        "ticker": [
               "GOOG",
               "MSFT",
               "MSFT",
               "MSFT",
               "GOOG",
               "AAPL",
               "GOOG",
               "MSFT"
           ],
           "bid": [720.50, 51.95, 51.97, 51.99, 720.50, 97.99, 720.50, 52.01],
           "ask": [720.93, 51.96, 51.98, 52.00, 720.93, 98.01, 720.88, 52.03]
    }
)
trades = pd.DataFrame(
       {
           "time": [
               pd.Timestamp("2016-05-25 13:30:00.023"),
               pd.Timestamp("2016-05-25 13:30:00.038"),
               pd.Timestamp("2016-05-25 13:30:00.047"),
               pd.Timestamp("2016-05-25 13:30:00.048"),
               pd.Timestamp("2016-05-25 13:30:00.048")
           ],
           "ticker": ["MSFT", "MSFT", "GOOG", "GOOG", "AAPL"],
           "price": [51.95, 51.95, 720.77, 720.92, 98.0],
           "quantity": [75, 155, 100, 100, 100]
       }
   )
print("===========报价数据=============")
print(quotes)
print("===========交易数据=============")
print(trades)
print("==============表连接，限定交易时间 - 报价时间 <= 2ms==============")
print(
pd.merge_asof(
    trades, quotes, on="time", tolerance=pd.Timedelta("2ms"), by='ticker'
))



# 输出结果如下
===========报价数据=============
                     time ticker     bid     ask
0 2016-05-25 13:30:00.023   GOOG  720.50  720.93
1 2016-05-25 13:30:00.023   MSFT   51.95   51.96
2 2016-05-25 13:30:00.030   MSFT   51.97   51.98
3 2016-05-25 13:30:00.041   MSFT   51.99   52.00
4 2016-05-25 13:30:00.048   GOOG  720.50  720.93
5 2016-05-25 13:30:00.049   AAPL   97.99   98.01
6 2016-05-25 13:30:00.072   GOOG  720.50  720.88
7 2016-05-25 13:30:00.075   MSFT   52.01   52.03
===========交易数据=============
                     time ticker   price  quantity
0 2016-05-25 13:30:00.023   MSFT   51.95        75
1 2016-05-25 13:30:00.038   MSFT   51.95       155
2 2016-05-25 13:30:00.047   GOOG  720.77       100
3 2016-05-25 13:30:00.048   GOOG  720.92       100
4 2016-05-25 13:30:00.048   AAPL   98.00       100
==============表连接，限定交易时间 - 报价时间 <= 2ms==============
                     time ticker   price  quantity     bid     ask
0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
1 2016-05-25 13:30:00.038   MSFT   51.95       155     NaN     NaN
2 2016-05-25 13:30:00.047   GOOG  720.77       100     NaN     NaN
3 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93
4 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN
```



### :b:分析

**`pd.merge_asof(trades, quotes, on="time", tolerance=pd.Timedelta("2ms"), by='ticker')`，执行过程如下：**

- **按`ticker`分组**
- **对于每个交易，在相同ticker的报价中查找时间上最近且不超过交易时间的报价**
- **只保留时间差在2毫秒以内的匹配**



**<span style='color: #51A7F9;font-size: 19px'>逐行分析结果</span>**

1. **第一行交易 (MSFT 13:30:00.023)**
   - 匹配报价中的 MSFT 13:30:00.023
   - 时间差：0ms ≤ 2ms → 匹配成功
   - 结果：bid=51.95, ask=51.96
2. **第二行交易 (MSFT 13:30:00.038)**
   - 最近的 MSFT 报价是 13:30:00.030 和 13:30:00.041
   - 向后查找 (direction='backward' 默认) 匹配 13:30:00.030
   - 时间差：8ms > 2ms → 超出 tolerance，不匹配
   - 结果：bid=NaN, ask=NaN
3. **第三行交易 (GOOG 13:30:00.047)**
   - 最近的 GOOG 报价是 13:30:00.023 和 13:30:00.048
   - 向后查找匹配 13:30:00.023
   - 时间差：24ms > 2ms → 超出 tolerance，不匹配
   - 结果：bid=NaN, ask=NaN
4. **第四行交易 (GOOG 13:30:00.048)**
   - 精确匹配 GOOG 13:30:00.048
   - 时间差：0ms ≤ 2ms → 匹配成功
   - 结果：bid=720.50, ask=720.93
5. **第五行交易 (AAPL 13:30:00.048)**
   - 最近的 AAPL 报价是 13:30:00.049
   - 向后查找无匹配 (报价时间在交易时间之后)
   - 结果：bid=NaN, ask=NaN









# 十一、时间序列分析

**Pandas有四个与时间相关的概念：**

- **Date times：带有时区的日期和时间，与标准库中的`datetime.datetime`相似**
- **Time deltas：一个固定的时间区间，与标准库中的`datetime.timedelta`**
- **Time spans：通过一个时间点和它的频率所定义的时间的跨度**
- **Date offsets：遵循日历算法的相对时间区间，与`dateutil`包中的`dateutil.relativedelta.relativedelta`相似**



|     概念     |    标量类    |      数组类      |                 Pandas数据类型                 |                 创建方法                  |
| :----------: | :----------: | :--------------: | :--------------------------------------------: | :---------------------------------------: |
|  Date times  | `Timestamp`  | `DatetimeIndex`  | `datetime64[ns]` 或 <br />`datetime64[ns, tz]` |     `to_datetime`或<br />`date_range`     |
| Time deltas  | `Timedelta`  | `TimedeltaIndex` |               `timedelta64[ns]`                | `to_timedelta` 或 <br />`timedelta_range` |
|  Time spans  |   `Period`   |  `PeriodIndex`   |                 `period[freq]`                 |     `Period` 或 <br />`period_range`      |
| Date offsets | `DateOffset` |      `None`      |                     `None`                     |               `DateOffset`                |



## 1、时间戳（`Timestamp`）

​		**Pandas里的时间戳相当于Python中的日期时间类型，它是构成日期索引的条目以及Pandas中其他面向时间序列的数据结构所使用的类型**



### （1）创建时间戳

#### pandas.Timestamp

**==pandas.Timestamp(*ts_input=\<object>, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, tzinfo=None, nanosecond=None, tz=None, unit=None, fold=None*)==**



| 参数： |
| ------ |

**①ts_input：datetime, str,int, float**

​	**要转换为时间戳的值**

**②year,month,day：int**

**③hour,minute,second,microsecond：int，可选，默认0**

**④tzinfo：时区信息**

**⑤nanosecond：int，可选，默认0**

**⑥tz：str，pytz.timezone, dateutil.tz.tzfile 或 None**



**三种不同的创建时间戳的方式**

```python
from datetime import datetime
print(pd.Timestamp(datetime(2012, 5, 1, 5, 24, 35)))
print(pd.Timestamp("2012-5-1 12:25:46"))
print(pd.Timestamp(2012, 5, 1, 10, 5, 14))


# 输出结果如下
2012-05-01 05:24:35
2012-05-01 12:25:46
2012-05-01 10:05:14
```





### （2）转换为时间戳

#### pandas.to_datetime

**==pandas.to_datetime(*arg, errors='raise', dayfirst=False, yearfirst=False, utc=False, format=None, exact=\<no_default>, unit=None, infer_datetime_format=\<no_default>, origin='unix', cache=True*)==**

​	**将arg参数转换为日期时间类型，此函数可以转换一个标量，类数组，Series或DataFrame/类字典，对于None/NaN/null，都会被转换成`NaT`**

**该函数支持多种输入类型，并产生不同的输出类型**

- **标量可以是int，float，str，datetime对象（来自标准库`datetime`或`numpy`中），返回`Timestamp`或`datetime.datetime`对象**
- **类数组可以包含int，float，str，datetime对象，返回`DatetimeIndex`或包含`datetime.datetime`的`Index`对象**
- **Series/DataFrame/类字典：返回`datetime64`的Series**



| 参数： |
| ------ |

**①arg：int，float，str，datetime，列表、元组、一维数组、Series、DataFrame或字典**

​	**要转换为日期时间的对象**

**②errors：{'ignore', 'raise', 'coerce'}，默认'raise'**

- **如果`'raise'`，则抛出异常**
- **如果`'coerce'`,则无效的转换被设置为`NaT`**
- **如果`'ignore'`，则忽略无效的转换**

**③dayfirst：bool，默认False**

​	**如果为True，则以欧洲日期格式解析**

**④yearfirst：bool，默认False**

​	**是否先解析年份**

**⑤format：str，默认None**

​	**指定解析日期的格式**

**⑥unit：str，默认'ns'**

​	**由arg参数决定，例如，使用`unit='ms'`和`origin='unix'`将计算自`1970-01-01`起的毫秒数**

**⑦origin：标量，默认'unix'**

​	**定义起始日期，数值将被解析为自参考日期以来的单位数（由unit参数定义）**

- **如果`'unix'`，则起始时间设置为`1970-01-01`**
- **如果`'julian'`，则`unit`必须为`D`，则起始时间设置为公元前4713年1月1日中午**
- **如果Timestamp可转换，则origin设置为由origin标识的Timestamp**
- **如果是浮点数或整数，则起始是相对于`1970-01-01`的差值**





```python
print("===============输入 arg参数 是一个标量，一般返回Timestamp对象====================")
print("*" * 100)
print("=========== 单个日期转换 ============")
a = pd.to_datetime("2010-12-10")
print(a, type(a))
print("============= 自定义格式日期转换 format=\"%m/%d/%Y\" =============")
b = pd.to_datetime("10/15/2014", format="%m/%d/%Y")
print(b, type(b))
print("==============标量是一个int类型，unit = 'ns'，这些表示从1970-01-01到某个时间经历的ns为int参数=====================")
c = pd.to_datetime(1490195805433502912, unit="ns")
print(c, type(c))
print()
print("===============输入 arg参数 是一个类列表，一般返回DatetimeIndex对象====================")
print("*" * 100)
print("=========== 欧洲格式的时间，需要指定dayfirst = True============")
print(pd.to_datetime(["04-01-2012 10:00"], dayfirst=True))
print("============= 日期列表转换 =============")
print(pd.to_datetime(["2018-01-01", "2018-01-03", "2018-01-05"]))
print("=========== 日期转换，将无法解析的对象转换为NaT,通过指定errors='coerce' ============")
print(pd.to_datetime(["2009/07/31", "asd"], errors="coerce"))
print("==============数组中的数据表示从1970-01-01到某个时间的秒数================")
print(pd.to_datetime([1490195805.433, 1490195805.433502912], unit="s"))
print("==============数组中的数据表示从2021-01-05往后推迟2/4/6个月================")
print(pd.to_datetime([2, 4, 6], unit="m", origin=pd.Timestamp("2021-01-05")))
print()
print("===============输入 arg参数 是一个DataFrame，返回Series====================")
print("*" * 100)
df = pd.DataFrame(
    {"year": [2015, 2016], "month": [2, 3], "day": [4, 5], "hour": [2, 3]}
)
print(df)
print(pd.to_datetime(df))



# 输出结果如下
===============输入 arg参数 是一个标量，一般返回Timestamp对象====================
****************************************************************************************************
=========== 单个日期转换 ============
2010-12-10 00:00:00 <class 'pandas._libs.tslibs.timestamps.Timestamp'>
============= 自定义格式日期转换 format="%m/%d/%Y" =============
2014-10-15 00:00:00 <class 'pandas._libs.tslibs.timestamps.Timestamp'>
==============标量是一个int类型，unit = 'ns'，这些表示从1970-01-01到某个时间经历的ns为int参数=====================
2017-03-22 15:16:45.433502912 <class 'pandas._libs.tslibs.timestamps.Timestamp'>


===============输入 arg参数 是一个类列表，一般返回DatetimeIndex对象====================
****************************************************************************************************
=========== 欧洲格式的时间，需要指定dayfirst = True============
DatetimeIndex(['2012-01-04 10:00:00'], dtype='datetime64[ns]', freq=None)
============= 日期列表转换 =============
DatetimeIndex(['2018-01-01', '2018-01-03', '2018-01-05'], dtype='datetime64[ns]', freq=None)
=========== 日期转换，将无法解析的对象转换为NaT,通过指定errors='coerce' ============
DatetimeIndex(['2009-07-31', 'NaT'], dtype='datetime64[ns]', freq=None)
==============数组中的数据表示从1970-01-01到某个时间的秒数================
DatetimeIndex(['2017-03-22 15:16:45.433000088', '2017-03-22 15:16:45.433502913'], dtype='datetime64[ns]', freq=None)
==============数组中的数据表示从2021-01-05往后推迟2/4/6个月================
DatetimeIndex(['2021-01-05 00:02:00', '2021-01-05 00:04:00',
               '2021-01-05 00:06:00'],
              dtype='datetime64[ns]', freq=None)


===============输入 arg参数 是一个DataFrame，返回Series====================
****************************************************************************************************
   year  month  day  hour
0  2015      2    4     2
1  2016      3    5     3
0   2015-02-04 02:00:00
1   2016-03-05 03:00:00
dtype: datetime64[ns]
```





## 2、偏移量和时间频率（`freq`）

​		**频率字符串（例如'D'）映射到DateOffset对象及其子类，DateOffset类似于TimeDelta，表示持续时间，但遵循特定的日历持续时间规则。例如，一个`Timedelta`日始终将`datetimes`递增24个小时，而一个`DateOffset`日可以将`datetime`增加到第二天相同的时间，无论一天是23、24还是25小时。但是，所有小于或等于一小时的`DateOffset`子类的行为都类似于`TimeDelta`**

​		**`DateOffset`可以将日期时间按指定的日历时长进行偏移，使用`+`算术运算符来执行偏移操作**

​		**大多数的`DateOffset`都和频率字符串或偏移量的别名有联系，它可以被传递给`freq`关键字参数。**



**`DateOffset`和`freq`字符串的联系如下：**

| Date Offset                                                  | Frequency String  | Description                                           |
| ------------------------------------------------------------ | ----------------- | ----------------------------------------------------- |
| [`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset) | None              | Generic offset class, defaults to absolute 24 hours   |
| [`BDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BDay.html#pandas.tseries.offsets.BDay) or [`BusinessDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.html#pandas.tseries.offsets.BusinessDay) | `'B'`             | 工作日                                                |
| [`CDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CDay.html#pandas.tseries.offsets.CDay) or [`CustomBusinessDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.html#pandas.tseries.offsets.CustomBusinessDay) | `'C'`             | 自定义工作日                                          |
| [`Week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Week.html#pandas.tseries.offsets.Week) | `'W'`             | 一周，可锚定这周的某一天                              |
| [`WeekOfMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.html#pandas.tseries.offsets.WeekOfMonth) | `'WOM'`           | 每个月的第几周的第几天                                |
| [`MonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.MonthEnd.html#pandas.tseries.offsets.MonthEnd) | `'ME'`            | calendar month end                                    |
| [`MonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.MonthBegin.html#pandas.tseries.offsets.MonthBegin) | `'MS'`            | calendar month begin                                  |
| [`BMonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BMonthEnd.html#pandas.tseries.offsets.BMonthEnd) or [`BusinessMonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html#pandas.tseries.offsets.BusinessMonthEnd) | `'BME'`           | business month end                                    |
| [`BMonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BMonthBegin.html#pandas.tseries.offsets.BMonthBegin) or [`BusinessMonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessMonthBegin.html#pandas.tseries.offsets.BusinessMonthBegin) | `'BMS'`           | business month begin                                  |
| [`SemiMonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthEnd.html#pandas.tseries.offsets.SemiMonthEnd) | `'SME'`           | 15th (or other day_of_month) and calendar month end   |
| [`SemiMonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthBegin.html#pandas.tseries.offsets.SemiMonthBegin) | `'SMS'`           | 15th (or other day_of_month) and calendar month begin |
| [`QuarterEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.QuarterEnd.html#pandas.tseries.offsets.QuarterEnd) | `'QE'`            | calendar quarter end                                  |
| [`QuarterBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.QuarterBegin.html#pandas.tseries.offsets.QuarterBegin) | `'QS'`            | calendar quarter begin                                |
| [`YearEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.YearEnd.html#pandas.tseries.offsets.YearEnd) | `'YE'`            | calendar year end                                     |
| [`YearBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.YearBegin.html#pandas.tseries.offsets.YearBegin) | `'YS'` or `'BYS'` | calendar year begin                                   |
| [`BusinessHour`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.html#pandas.tseries.offsets.BusinessHour) | `'bh'`            | 工作时间                                              |
| [`CustomBusinessHour`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.html#pandas.tseries.offsets.CustomBusinessHour) | `'cbh'`           | 自定义工作时间                                        |
| [`Day`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Day.html#pandas.tseries.offsets.Day) | `'D'`             | 一天                                                  |
| [`Hour`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Hour.html#pandas.tseries.offsets.Hour) | `'h'`             | 一小时                                                |
| [`Minute`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Minute.html#pandas.tseries.offsets.Minute) | `'min'`           | 一分钟                                                |
| [`Second`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Second.html#pandas.tseries.offsets.Second) | `'s'`             | 一秒                                                  |
| [`Milli`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Milli.html#pandas.tseries.offsets.Milli) | `'ms'`            | 一毫秒                                                |
| [`Micro`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Micro.html#pandas.tseries.offsets.Micro) | `'us'`            | 一微秒                                                |
| [`Nano`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Nano.html#pandas.tseries.offsets.Nano) | `'ns'`            | 一纳秒                                                |





### （1）时间偏移（`DateOffset`）

#### class pandas.tseries.offsets.DateOffset

​	**用于日期范围的标准日期增量。**

​	**DateOffset的工作原理如下，每个偏移量指定一组符合DateOffset的日期，例如，BDay 将此集合定义为工作日的日期集合。要测试某个日期是否在DateOffset的集合中，可以使用 `dateOffset.is_on_offset(date)`。**

​	**若日期不是有效日期，则可以使用  ==rollback(dt)==  和  ==rollforword(dt)==  将日期向后或向前滚动**

​	**可以通过创建DateOffset来将日期向前滚动或向后滚动给定数量的日期，其伪代码如下**

​	:a:**偏移量 n>0：**

```python
def __add__(date):
    date = rollback(date)
    return date + <n number of periods>
```

​	**:b:偏移量 n<0：**

```python
def __add__(date):
    date = rollforward(date)
    return date + <n number of periods>
```





### （2）频率（`freq`）

#### :a:一般偏移量

|    别名    |          描述          |
| :--------: | :--------------------: |
|    `B`     |         工作日         |
|    `C`     |      自定义工作日      |
|    `D`     |         自然日         |
| `W/M/Q/Y`  | 每周/每月/每季度/每年  |
|    `ME`    |        每个月末        |
|   `SME`    | 每个半月（15日和月末） |
|    `MS`    |        每个月初        |
|    `QE`    |       每个季度末       |
|    `QS`    |       每个季度初       |
|    `YE`    |         每年末         |
|    `YS`    |         每年初         |
|    `h`     |         每小时         |
|    `bh`    |       每个工作时       |
|   `min`    |         每分钟         |
|    `s`     |          每秒          |
| `ms/us/ns` |    每毫秒/微秒/纳秒    |



#### :b:锚定偏移量

|                别名                |                   说明                    |
| :--------------------------------: | :---------------------------------------: |
|       `W-SUN/W-MON/W-TUE...`       |         每周日/每周一/每周二 ...          |
| `(B)Q(E)(S)-DEC/(B)Q(E)(S)-JAN...` | 季度频率，指定十二月/一月为一年的季度结束 |
| `(B)Y(E)(S)-DEC/(B)Y(E)(S)-JAN...` |  每（工作）年十二月/一月（末）（初）...   |



## pandas.date_range

**==pandas.date_range(*start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, inclusive='both', unit=None*)==**

​	**返回固定频率的DatetimeIndex**

​	**返回等距时间点的范围（其中任意两个相邻点之间的差由给定的频率指定），使得它们都满足 $start \le x \le end$。**

​	**在`start`,`end`,`periods`和`freq`四个参数之中，必须精确的指定三个参数**



| 参数： |
| ------ |

**①start/end：str 或 datetime，可选**

​	**生成的日期要从何时开始/结束**

**②periods：int，可选**

​	**要生成的周期数**

**③freq：str，Timedelta, datetime.timedelta, 或DateOffset，默认'D'**

​	**频率字符串可以包含多个，例如'5h'**

**④tz：str 或 tzinfo，可选**

​	**指定的时区信息**

**⑤normalize：bool，默认False**

​	**是否把开始/结束时间标准化为午夜（0:0:0）**

**⑥inclusive：{"both", "neither", "left", "right"}，默认"both"**

​	**指定是否包含边界**

**⑦unit：str，默认None**

​	**指定结果所需的精度**



```python
print("============ 指定开始和结束时间，默认频率是天 =============")
print(pd.date_range(start='2010-01-01', end='2010-01-08'))
print("============ 指定开始时间，往后延8天 periods = 8 =============")
print(pd.date_range(start='2010-01-01', periods=8))
print("============ 指定结束时间，往前推6天 periods = 6 =============")
print(pd.date_range(end='2010-01-08', periods=6))
print("============ 指定开始和结束的时间，默认包含两边 =============")
print(pd.date_range(start='2010-01-01', end='2010-01-09'))
print("============ 指定开始和结束的时间，只包含左边界 inclusive = left =============")
print(pd.date_range(start='2010-01-01', end='2010-01-09', inclusive="left"))
print("============ 指定开始和结束的时间，只包含右边界 inclusive = right =============")
print(pd.date_range(start='2010-01-01', end='2010-01-09', inclusive="right"))
print("============ 指定开始和结束的时间，不包含左右边界 inclusive = neither =============")
print(pd.date_range(start='2010-01-01', end='2010-01-09', inclusive="neither"))
print("============ 一般的偏移量 =============")
print("*" * 100)
print("============ 指定开始时间，周期为5，频率设置为月末 =============")
print(pd.date_range(start='2010-01-01', periods=5, freq="ME"))
print("============ 指定开始时间，周期为5，频率设置为季度开始 =============")
print(pd.date_range(start='2010-01-01', periods=5, freq="QS"))
print("============ 指定开始时间，周期为5，频率设置为月初 =============")
print(pd.date_range(start='2010-01-15', periods=5, freq="MS"))
print("============ 锚定偏移量 =============")
print("*" * 100)
print("============ 指定开始时间，周期为5，频率设置为两周 =============")
print(pd.date_range(start='2010-01-15', periods=5, freq="2W"))
print("============ 指定开始时间，周期为5，频率设置为三天 =============")
print(pd.date_range(start='2010-01-15', periods=5, freq="3D"))
print("============ 指定开始时间，周期为5，频率设置为3分钟 =============")
print(pd.date_range(start='2010-01-15', periods=5, freq="3min"))
print("============ 指定开始时间，周期为5，频率设置为每周三 =============")
print(pd.date_range(start='2010-01-15', periods=5, freq="W-TUE"))
print("============ 指定开始时间，周期为5，频率设置为每年年初，以十二月为年初 =============")
print(pd.date_range(start='2010-01-15', periods=5, freq="YS-SEP"))




# 输出结果如下
============ 指定开始和结束时间，默认频率是天 =============
DatetimeIndex(['2010-01-01', '2010-01-02', '2010-01-03', '2010-01-04',
               '2010-01-05', '2010-01-06', '2010-01-07', '2010-01-08'],
              dtype='datetime64[ns]', freq='D')
============ 指定开始时间，往后延8天 periods = 8 =============
DatetimeIndex(['2010-01-01', '2010-01-02', '2010-01-03', '2010-01-04',
               '2010-01-05', '2010-01-06', '2010-01-07', '2010-01-08'],
              dtype='datetime64[ns]', freq='D')
============ 指定结束时间，往前推6天 periods = 6 =============
DatetimeIndex(['2010-01-03', '2010-01-04', '2010-01-05', '2010-01-06',
               '2010-01-07', '2010-01-08'],
              dtype='datetime64[ns]', freq='D')
============ 指定开始和结束的时间，默认包含两边 =============
DatetimeIndex(['2010-01-01', '2010-01-02', '2010-01-03', '2010-01-04',
               '2010-01-05', '2010-01-06', '2010-01-07', '2010-01-08',
               '2010-01-09'],
              dtype='datetime64[ns]', freq='D')
============ 指定开始和结束的时间，只包含左边界 inclusive = left =============
DatetimeIndex(['2010-01-01', '2010-01-02', '2010-01-03', '2010-01-04',
               '2010-01-05', '2010-01-06', '2010-01-07', '2010-01-08'],
              dtype='datetime64[ns]', freq='D')
============ 指定开始和结束的时间，只包含右边界 inclusive = right =============
DatetimeIndex(['2010-01-02', '2010-01-03', '2010-01-04', '2010-01-05',
               '2010-01-06', '2010-01-07', '2010-01-08', '2010-01-09'],
              dtype='datetime64[ns]', freq='D')
============ 指定开始和结束的时间，不包含左右边界 inclusive = neither =============
DatetimeIndex(['2010-01-02', '2010-01-03', '2010-01-04', '2010-01-05',
               '2010-01-06', '2010-01-07', '2010-01-08'],
              dtype='datetime64[ns]', freq='D')



============ 一般的偏移量 =============
****************************************************************************************************
============ 指定开始时间，周期为5，频率设置为月末 =============
DatetimeIndex(['2010-01-31', '2010-02-28', '2010-03-31', '2010-04-30',
               '2010-05-31'],
              dtype='datetime64[ns]', freq='ME')
============ 指定开始时间，周期为5，频率设置为季度开始 =============
DatetimeIndex(['2010-01-01', '2010-04-01', '2010-07-01', '2010-10-01',
               '2011-01-01'],
              dtype='datetime64[ns]', freq='QS-JAN')
============ 指定开始时间，周期为5，频率设置为月初 =============
DatetimeIndex(['2010-02-01', '2010-03-01', '2010-04-01', '2010-05-01',
               '2010-06-01'],
              dtype='datetime64[ns]', freq='MS')



============ 锚定偏移量 =============
****************************************************************************************************
============ 指定开始时间，周期为5，频率设置为两周 =============
DatetimeIndex(['2010-01-17', '2010-01-31', '2010-02-14', '2010-02-28',
               '2010-03-14'],
              dtype='datetime64[ns]', freq='2W-SUN')
============ 指定开始时间，周期为5，频率设置为三天 =============
DatetimeIndex(['2010-01-15', '2010-01-18', '2010-01-21', '2010-01-24',
               '2010-01-27'],
              dtype='datetime64[ns]', freq='3D')
============ 指定开始时间，周期为5，频率设置为3分钟 =============
DatetimeIndex(['2010-01-15 00:00:00', '2010-01-15 00:03:00',
               '2010-01-15 00:06:00', '2010-01-15 00:09:00',
               '2010-01-15 00:12:00'],
              dtype='datetime64[ns]', freq='3min')
============ 指定开始时间，周期为5，频率设置为每周三 =============
DatetimeIndex(['2010-01-19', '2010-01-26', '2010-02-02', '2010-02-09',
               '2010-02-16'],
              dtype='datetime64[ns]', freq='W-TUE')
============ 指定开始时间，周期为5，频率设置为每年年初，以十二月为年初 =============
DatetimeIndex(['2010-09-01', '2011-09-01', '2012-09-01', '2013-09-01',
               '2014-09-01'],
              dtype='datetime64[ns]', freq='YS-SEP')
```





## pandas.period_range

**==pandas.period_range(*start=None, end=None, periods=None, freq=None, name=None*)==**

​	**返回一个固定频率的PeriodIndex**



| 参数： |
| ------ |

**①start/end：str，datetime，date，pandas.Timestamp，或period，默认None**

​	**生成周期的左/右边界**

**②periods：int，默认None**

​	**生成的周期数量**

**③freq：str 或 DateOffset，可选**

​	**频率，默认为'D'**

**④name：str，默认None**

​	**结果PeriodIndex的名字**



| 返回值： |
| -------- |

**:arrow_right:返回PeriodIndex**



```python
>>> pd.period_range(start='2017-01-01', end='2018-01-01', freq='M')
PeriodIndex(['2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06',
         '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12',
         '2018-01'],
        dtype='period[M]')
```



## Period.asfreq

**==Period.asfreq(*freq, how='E'*)==**

​	**使用指定的频率转换周期**



| 参数： |
| ------ |

**①freq：str，BaseOffset**

​	**期望转换的频率**

**②how：{'E', 'S', 'end', 'start'}，默认'end'**

​	**时间跨度的开始或结束**



| 返回值： |
| -------- |

**:arrow_right:重采样的Period**



```python
>>> period = pd.Period('2023-1-1', freq='D')
>>> period.asfreq('h')
Period('2023-01-01 23:00', 'h')
```



## 3、重采样及频率转换

**重采样指的是将时间序列从一个频率转换到另一个频率的处理过程，高频率转为低频率称为降采样，低频率转为高频率称为升采样。pandas中使用resample方法，进行重采样**

**例如：**

```python
dates = pd.date_range("2000-01-01", periods=100)
ts = pd.Series(np.random.standard_normal(len(dates)), index=dates)
ts
ts.resample("ME").mean()  # ME Month-End
ts.resample("ME").mean().to_period('M')  # 转成周期索引


# 输出结果如下
2000-01    0.080048
2000-02    0.209347
2000-03    0.205797
2000-04    0.318330
Freq: M, dtype: float64
```



**在金融领域，一种常用的时间序列聚合方式是计算各个桶的4个值，即第一个值（open，开盘）、最后一个值（close，收盘）、最大值（high，最高）以及最小值（low，最低）。通过==ohlc==聚合函数，即可得到一个含有这4种聚合值的DataFrame，整个过程很高效，只需经过一次函数调用：**

```python
>>> lst = ['SPX', 'CAC', 'SPX', 'CAC', 'SPX', 'CAC', 'SPX', 'CAC',]
>>> ser = pd.Series([3.4, 9.0, 7.2, 5.2, 8.8, 9.4, 0.1, 0.5], index=lst)
>>> ser
SPX     3.4
CAC     9.0
SPX     7.2
CAC     5.2
SPX     8.8
CAC     9.4
SPX     0.1
CAC     0.5
dtype: float64
>>> ser.groupby(level=0).ohlc()
     open  high  low  close
CAC   9.0   9.4  0.5    0.5
SPX   3.4   8.8  0.1    0.1
```











# # 概率论与数理统计

## # 分位数

**给定一个数据集 $X = {x_1, x_2,..., x_n}$，$p$-分位数（$0 \leq p \leq 1$）是一个值$Q_p$，**

**使得：**

​		**至少有$p \times 100\% $的数据 $\leq Q_p$，有$(1-p) \times 100\%$的数据$\geq Q_p$** 

**也就是说，$p$-分位数满足：**
$$
P\{X \leq Q_p\} = p
$$
**则我们称 $Q_p$ 为数据集$X$的分位数**



**其中：常用的分位数为50%（也叫样本的中位数）、25%和75%（四分位数）**

​			**你可以通过Pandas中的`quantile`方法计算任意的分位数，例如`df.quantile(0.1)`**



**分位数如图所示：**

![](G:\01资料\Pictures\p分位数.png)







## # 样本的中心距

**对于一组样本数据$x_1, x_2, ..., x_n$，其k阶样本中心距定义为：**
$$
m_k = \frac{1}{n} \sum_{i=1}^n(x_i  - \bar{x})^k
\\其中：\ \ \ \  \bar{x} = \frac{1}{n} \sum_{i=1}^nx_i(样本均值) \ \ ,k是阶数
$$


**:one:一阶中心距（$k=1$）： 恒等于0**
$$
m_1 = \frac{1}{n} \sum_{i=1}^n(x_i - \bar{x}) \\
=  \frac{1}{n}( \sum_{i=1}^n x_i - \sum_{i=1}^n\bar{x}) \\
=	\frac{1}{n}( \sum_{i=1}^n x_i - n\bar{x}) \ \ \\
=  \frac{1}{n}( \sum_{i=1}^n x_i - \sum_{i=1}^n x_i) =0
$$


**:two:二阶中心距（k=2）**

​	**样本的方差，描述数据的离散程度**
$$
m_2 = \frac{1}{n} \sum_{i=1}^n(x_i - \bar{x})^2 \\
$$


**:three:三阶中心距（k=3）**

​	**样本的偏度，描述分布的不对称性**
$$
m_3 = \frac{1}{n} \sum_{i=1}^n(x_i - \bar{x})^3 \\
$$


**:four:四阶中心距（k=4）**

​	**样本的峰度，描述分布的陡峭程度**
$$
m_4 = \frac{1}{n} \sum_{i=1}^n(x_i - \bar{x})^4 \\
$$




## # 协方差与相关系数

### 1、协方差 ###

$$
\mathrm{Cov}(X, Y) = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})
$$

**一些性质：**
$$
\mathrm{Cov}(X, a) = 0 \ (a是常数)\\ \\
\mathrm{Cov}(X, X) = Var(X) \\
\mathrm{Cov}(X, Y) = \mathrm{Cov}(Y, X) \\ \\
\mathrm{Cov}(aX, bY) = ab\mathrm{Cov}(X, Y)\\
\mathrm{Cov}(X+a, Y+b) = \mathrm{Cov}(X, Y)
$$




### 2、相关系数

$$
r = \frac{\mathrm{Cov}(X,Y)}{\sigma_X \sigma_Y} \ \ \ \ \  r \in [-1, 1]
$$

- **$r = 1$ 表示X和Y完全正相关**

- **$r = -1$ 表示X和Y完全负相关**
- **$r = 0$ 表示X和Y无线性相关性**



### 3、协方差矩阵

**给定一个随机向量$\mathbf{X} = [X_1, X_2, ..., X_n]^T$，其均值向量为$\mu = [EX_1, EX_2, ..., EX_n]^T$，协方差矩阵定义为**
$$
\Sigma = E[(\mathbf{X} - \mu)(\mathbf{X}-\mu)^T] \\
$$
**其中：**
$$
\Sigma_{ij} = \mathrm{Cov}(X_i,X_j) = E[(X_i-\mu_i)(X_j-\mu_j)]
$$
**具体形式如下：**
$$
\Sigma = \begin{bmatrix}
\text{Var}(X_1) & \text{Cov}(X_1, X_2) & \cdots & \text{Cov}(X_1, X_n) \\
\text{Cov}(X_2, X_1) & \text{Var}(X_2) & \cdots & \text{Cov}(X_2, X_n) \\
\vdots & \vdots & \ddots & \vdots \\
\text{Cov}(X_n, X_1) & \text{Cov}(X_n, X_2) & \cdots & \text{Var}(X_n)
\end{bmatrix}
$$
**协方差矩阵由如下性质：**

- **对称性：$\Sigma^T = \Sigma$，因为$\mathrm{Cov}(X, Y) = \mathrm{Cov}(Y,X)$**
- **半正定性：对于任意的非零向量$\mathbf{x}$，都有$\mathbf{x}^T\Sigma\mathbf{x} \geq 0$**
- **可相似对角化：存在正交矩阵 $Q$ ，使得$Q^T\Sigma Q = \Lambda \iff \Sigma = (Q^T)^{-1} \Lambda  Q^{-1}$，即协方差矩阵的奇异值分解（用于主成分分析）**





# #背景知识

## # 独热编码（one-hot）

​	**独热 在数字电路和机器学习中被用来表示一种特殊的比特组或向量，该字节或向量里仅允许其中一位为1，其他位都必须为0。若情况相反，则称为独冷。**

​	**在统计学中，虚拟变量（dummy variable，又称哑变量）代表了类似的概念，它用来表示一个定性的事实，从而将数据分为互斥的类型（如吸烟者和非吸烟者）**



**应用：**

**:a:有限状态机**

​	**独热码尝尝被用来表示一个有限状态机的状态，如果使用二进制来代表状态，则需要用到解码器才能得知该二进制码代表的状态。使用独热码来代表状态的话，则不需要解码器。因为若第$n$个比特为1，就代表机器目前在第$n$个状态，如下表所示**

| 二进制 | 独热码（one-hot） |  状态   |
| :----: | :---------------: | :-----: |
|  000   |     0000 0001     |  :one:  |
|  001   |     0000 0010     |  :two:  |
|  010   |     0000 0100     | :three: |
|  011   |     0000 1000     | :four:  |
|  100   |     0001 0000     | :five:  |
|  101   |     0010 0000     |  :six:  |
|  110   |     0100 0000     | :seven: |
|  111   |     1000 0000     | :eight: |



**:b:自然语言处理**

​	**在自然语言处理中，如有个字典或字库里有$N$个单字，则每个单字可以被一个$N$维的独热向量代表。**

​	**例如，若字库里仅有apple，banana以及pineapple这三个单字，则他们的独热向量可以为：**
$$
apple &= [1 \ 0 \ 0] \\
banana &= [0 \ 1 \ 0] \\
pineapple &= [0 \ 0 \ 1] \\
$$
​	**因为电脑无法理解非数字类的数据，独热编码可以将类别性的数据转换成统一的数字格式，方便处理和计算。而转换成固定维度的向量则方便机器学习的算法进行线性代数上的计算。独热编码可以采取稀疏矩阵的数据结构存储，以节省存储空间**





## # 正则表达式

**正则表达式是一种用简单字符串来描述、匹配文中全部匹配指定格式的字符串**

**正则表达式的优先级**

| 优先级 |                  符号                   |
| :----: | :-------------------------------------: |
|  最高  |                   `\`                   |
|   高   |       `()`、`(?:)`、`(?=)`、`[]`        |
|   中   | `*`、`+`、`?`、`{n}`、`{n, }`、`{n, m}` |
|   低   |           `^`、`$`、中介字符            |
| 次最低 |       串接，即相邻字符连接在一起        |
|  最低  |                   `|`                   |



**正则表达式的语法**

|          字符           |                             规则                             |
| :---------------------: | :----------------------------------------------------------: |
|           `+`           |         代表前面的字符必须至少出现一次（1次或多次）          |
|           `?`           |          代表前面的字符最多只可出现一次（0次或1次）          |
|           `*`           | 代表前面的字符可以不出现，也可以出现一次或多次（0次、1次或多次） |
|          `()`           |                   定义操作符的范围和优先度                   |
|          `[]`           |         字符的集合，匹配该集合中所包含的任意一个字符         |
| `{n}`、`{n,}`、`{n, m}` | 分别代表匹配确定的$n$次，至少匹配$n$次和最少匹配$n$次且最多匹配$m$次，其中$n,m \ge0$ |
|           `^`           |                   匹配输入字符串的开始位置                   |
|           `$`           |                     匹配字符串的结束位置                     |
|           `|`           |                          表示逻辑或                          |



## Python中的正则表达式操作

**一个正则表达式通常被称为一个pattern，是用来描述或者匹配一系列匹配某个句法规则的字符串**

**Python中的支持正在表达式的模块为re模块**

### re.compile

**==re.compile(*pattern, flags=0*)==**

​	**将正则表达式的样式编译为一个正则表达式对象(`Class re.Pattern`)，可以用于匹配，表达式的行为可以通过指定 *flags* 值来修改。**

```python
import re
prog = re.compile(pattern)
result = prog.match(string)
```

**等价于**

```python
result = re.match(pattern, string)
```

**如果需要多次使用这个正则表达式的话，使用`re.compile()`可以保存这个对象以便复用**



### re.search

**==re.search(*pattern, string, flags=0*)==**

**==Pattern.search(*string[, pos[, endpos]]*)==**

​	**扫描整个 *string* 查找与正则表达式 *pattern*匹配的第一个位置，并返回相应的匹配对象；如果没有匹配成功，则返回None **



### re.match

**==re.match(*pattern, string, flags=0*)==**

**==Pattern.match(*string[, pos[, endpos]]*)==**

​	**如果 *string* 开头的零个或多个字符与正则表达式 *pattern* 匹配，则返回相应的匹配对象，否在返回None，只匹配开始位置**



### re.match vs re.search

- **`re.match()`只在字符串的开头位置检测匹配**
- **`re.search()`在字符串中的任何位置检测匹配**
- **`re.fullmatch()`检测整个字符串是否匹配**

```python
>>> re.match("c", "abcdef")    # 不匹配
>>> re.search("c", "abcdef")   # 匹配
<re.Match object; span=(2, 3), match='c'>
>>> re.fullmatch("p.*n", "python") # 匹配
<re.Match object; span=(0, 6), match='python'>
>>> re.fullmatch("r.*n", "python") # 不匹配
```



**对于多行模式的正则表达式，`re.match()`也只是匹配字符串的开始，但使用`re.search()`和以`^`开始的正则表达式会匹配每行的开始，例如：**

```python
>>> re.match("X", "A\nB\nX", re.MULTILINE)		#不匹配
>>> re.search("^X", "A\nB\nX", re.MULTILINE)	#匹配
<re.Match object; span=(4, 5), match='X'>
```





### re.split

**==re.split(*pattern, string, maxsplit=0, flags=0*)==**

**==Pattern.split(*string, maxsplit=0*)==**

​	**使用 *pattern* 分开 *string*; 如果 *pattern* 里面有括号，那么所有组里的文字都会包含在列表里。如果 *maxsplit*非0，最多进行 *maxisplit*此分隔，剩下的字符全部返回到列表的最后一个元素中。**



```python
>>> re.split(r'\W+', 'Words, words, words.')
['Words', 'words', 'words', '']
>>> re.split(r'(\W+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split(r'\W+', 'Words, words, words.', maxsplit=1)
['Words', 'words, words.']
>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']
```

**`\W`（大写W）：匹配不属于单词类字符的任意字符，即字符串中的所有字符都不是字母或数字**



### re.findall

**==re.findall(*pattern, string, flags=0*)==**

**==Pattern.findall(*string, [, pos[, endpos]]*)==**

​	**返回 *pattern* 在 *string*中的所有非重叠匹配，以字符串列表或字符串元组列表的形式返回。**

​	**Pattern调用可限制搜索范围**



```python
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')		#\b 匹配空字符串
['foot', 'fell', 'fastest']
>>> re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
[('width', '20'), ('height', '10')]
```

**`\w`(小写w)：匹配字符串中的字母或数字，等价于`[a-zA-Z0-9_]`**



**查找所有副词**

```python
text = "He was carefully disguised but captured quickly by police."
>>> re.findall(r"\w+ly\b", text)
['carefully', 'quickly']
```

**`\b`只在开头和结尾，匹配空字符串**



### re.sub

**==re.sub(*pattern, repl, string, count=0, flags=0*)==**

​	**返回通过使用*repl*替换在*string*最左边非重叠出现的*pattern*而获得的字符串，如果未找到匹配的正则表达式，则返回原*string*；**

​	***repl*可以是字符串或函数；**

- **如果为字符串，则其中任何反斜杠转义序列都会被处理。也就是说，`\n`表示换行符，`\r`表示一个回车符**
- **如果是一个函数，则它会针对每次*pattern*的非重叠出现的情况被调用，该函数接受单个匹配对象参数，并返回替换字符串**

​	**可选参数*count*是要替换的最大次数**



```python
def dashrepl(matchobj):
    if matchobj.group(0) == '-': return ' '
    else: return '-'
>>> re.sub('-{1,2}', dashrepl, 'pro----gram-files')
'pro--gram files'

>>> re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
'Baked Beans & Spam'
```







# # 常用方法

## # 重新索引/排序/选择

### Series/DataFrame.reindex

**==DataFrame.reindex(*labels=None, index=None, columns=None, axis=None, method=None, copy=None, level=None, fill_value=nan, limit=None*)==**

​	**重新索引，使用可选的填充逻辑将DataFrame与新索引一致。如果新的索引没有在原数据的索引中，则会填充NA值，如果原数据中有重复索引则引发ValueError**



| 参数： |
| ------ |

**①labels: array_like, 可选**

​	**新的标签/索引**

**②index：array_like，可选**

​	**索引的新标签，为了避免重复，最好使用Index对象**

**③columns: array_like, 可选**

​	**列的新标签，为了避免重复，最好使用Index对象**

**④axis: int或str，可选**

​	**目标轴，可以是轴名称（`index`, `columns`）或数字0,1**

**⑤method: {None, 'backfill'/'bfill', 'pad'/'ffill', 'nearest'}**

​	**用于填充DataFrame中的缺失值的方法；请注意：此方法仅适用于具有单调递增/递减索引的DataFrame/Series**

- **默认为None：不填充缺失值**
- **pad/ffill：使用最后一个/一组数据填充缺失值**
- **backfill/bfill：使用下一个有效观察填充空白**
- **nearest：使用最近的有效观测值填补空白**

**⑥copy：bool，默认为True**

​	**返回一个新对象，即使传递的索引相同**

**⑦level： int 或 name**

​	**通过level广播，在MultiIndex级别上匹配索引值**

**⑧fill_value：标量，默认为np.nan**

​	**用于填充缺失值的值**

**⑨limit：int，默认None**

​	**向前或向后填充的最大连续元素数**



| 返回值： |
| -------- |

**:arrow_right:返回已更改索引的DataFrame**



```python
#对DataFrame的索引（行标签）做操作
----------------------------------------------------------------------------------
df = pd.DataFrame(np.arange(15).reshape((5, 3)),
                  index=list('abcde'),
                  columns=["A", "B", "C"])
print(df)
print("=============使用位置参数填充，默认填充DataFrame的索引=====================")
print(df.reindex(['a', 'f','b', 'g', 'c', 'h', 'd', 'e']))
print("=============使用axis参数,指定填充的轴为index=====================")
print(df.reindex(['a', 'f','b', 'g', 'c', 'h', 'd', 'e'], axis='index'))
print("=============使用关键字参数填充DataFrame的索引=====================")
print(df.reindex(index=['a', 'f','b', 'g', 'c', 'h', 'd', 'e']))
print("=============使用pad/ffill填充缺失值=====================")
print(df.reindex(index=['a', 'f','b', 'g', 'c', 'h', 'd', 'e'], method="ffill"))
print("=============使用backfill/bfill填充缺失值=====================")
print(df.reindex(index=['a', 'f','b', 'g', 'c', 'h', 'd', 'e'], method="bfill"))
print("=============设置填充值为0(int64)=====================")
print(df.reindex(index=['a', 'f','b', 'g', 'c', 'h', 'd', 'e'], fill_value=0))


    A   B   C
a   0   1   2
b   3   4   5
c   6   7   8
d   9  10  11
e  12  13  14
=============使用位置参数填充，默认填充DataFrame的索引=====================
      A     B     C
a   0.0   1.0   2.0
f   NaN   NaN   NaN
b   3.0   4.0   5.0
g   NaN   NaN   NaN
c   6.0   7.0   8.0
h   NaN   NaN   NaN
d   9.0  10.0  11.0
e  12.0  13.0  14.0
=============使用axis参数,指定填充的轴为index=====================
      A     B     C
a   0.0   1.0   2.0
f   NaN   NaN   NaN
b   3.0   4.0   5.0
g   NaN   NaN   NaN
c   6.0   7.0   8.0
h   NaN   NaN   NaN
d   9.0  10.0  11.0
e  12.0  13.0  14.0
=============使用关键字参数填充DataFrame的索引=====================
      A     B     C
a   0.0   1.0   2.0
f   NaN   NaN   NaN
b   3.0   4.0   5.0
g   NaN   NaN   NaN
c   6.0   7.0   8.0
h   NaN   NaN   NaN
d   9.0  10.0  11.0
e  12.0  13.0  14.0
=============使用pad/ffill填充缺失值=====================
    A   B   C
a   0   1   2
f  12  13  14
b   3   4   5
g  12  13  14
c   6   7   8
h  12  13  14
d   9  10  11
e  12  13  14
=============使用backfill/bfill填充缺失值=====================
      A     B     C
a   0.0   1.0   2.0
f   NaN   NaN   NaN
b   3.0   4.0   5.0
g   NaN   NaN   NaN
c   6.0   7.0   8.0
h   NaN   NaN   NaN
d   9.0  10.0  11.0
e  12.0  13.0  14.0
=============设置填充值为0(int64)=====================
    A   B   C
a   0   1   2
f   0   0   0
b   3   4   5
g   0   0   0
c   6   7   8
h   0   0   0
d   9  10  11
e  12  13  14



#对DataFrame的列标签做操作
----------------------------------------------------------------------------------

print("=============使用axis参数,指定填充的轴为columns=====================")
print(df.reindex(['A', 'B', 'D'], axis='columns'))
print("=============使用关键字参数填充DataFrame的列标签=====================")
print(df.reindex(columns=['A', 'B', 'D'], fill_value="missing"))
print("=============使用pad/ffill填充缺失值=====================")
print(df.reindex(columns=['A', 'B', 'D'], method="ffill"))
print("=============使用backfill/bfill填充缺失值=====================")
print(df.reindex(columns=['A', 'B', 'D'], method="bfill"))

=============使用axis参数,指定填充的轴为columns=====================
    A   B   D
a   0   1 NaN
b   3   4 NaN
c   6   7 NaN
d   9  10 NaN
e  12  13 NaN
=============使用关键字参数填充DataFrame的列标签=====================
    A   B        D
a   0   1  missing
b   3   4  missing
c   6   7  missing
d   9  10  missing
e  12  13  missing
=============使用pad/ffill填充缺失值=====================
    A   B   D
a   0   1   2
b   3   4   5
c   6   7   8
d   9  10  11
e  12  13  14
=============使用backfill/bfill填充缺失值=====================
    A   B   D
a   0   1 NaN
b   3   4 NaN
c   6   7 NaN
d   9  10 NaN
e  12  13 NaN

```





### Series/DataFrame.head

**==DataFrame.head(*n=5*)==**

​	**返回DataFrame对象的前n行，默认为5。**

​	**如果n<0，则返回除最后$|n|$行之外的所有行，等价于`df[:n]`；**

​	**如果`n>len(df)`，则返回所有行**

```python
>>> df = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion',
...                    'monkey', 'parrot', 'shark', 'whale', 'zebra']})
>>> df
      animal
0  alligator
1        bee
2     falcon
3       lion
4     monkey
5     parrot
6      shark
7      whale
8      zebra

>>> df.head()				#返回前五行
      animal
0  alligator
1        bee
2     falcon
3       lion
4     monkey

>>> df.head(3)				#返回前三行
      animal
0  alligator
1        bee
2     falcon

>>> df.head(-3)				#查看除最后三行之外的所有行，等价于df[:-3],从第一行到倒数第三行（不包含-3）
      animal
0  alligator
1        bee
2     falcon
3       lion
4     monkey
5     parrot
```





### Series/DataFrame.tail

**==DataFrame.tail(*n=5*)==**

​	**返回DataFrame对象的最后n行**

​	**如果`n<0`，则返回除前$|n|$ 行之外的所有行，等价于`df[|n|:]`**

​	**如果`n>len(df)`，则返回所有行**

```python
>>> df = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion',
...                    'monkey', 'parrot', 'shark', 'whale', 'zebra']})
>>> df
      animal
0  alligator
1        bee
2     falcon
3       lion
4     monkey
5     parrot
6      shark
7      whale
8      zebra

>>> df.tail()			 #查看最后五行
   animal
4  monkey
5  parrot
6   shark
7   whale
8   zebra

>>> df.tail(3)				#查看最后三行
  animal
6  shark
7  whale
8  zebra

>>> df.tail(-3)				#查看除前三行之外的所有行，即df[3:]
   animal
3    lion
4  monkey
5  parrot
6   shark
7   whale
8   zebra
```





### Series/DataFrame.sort_index

**==DataFrame.sort_index(*axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, ignore_index=False, key=None*)==**

​	**对行/列索引进行排序，默认对行索引排序（沿着0轴）**



| 参数： |
| ------ |

**①axis：{0 或 'index'，1 或 'columns'}，默认轴0**

​	**要沿哪个轴排序**

**②level：int 或 等级名 或 整数列表 或等级名列表**

​	**指定在索引的哪个层级上排序**

**③ascending：bool 或 布尔值列表，默认为True**

​	**按升序或降序排序。当索引为多级索引时，可以单独控制每个级别的排序方向**

**④inplace: bool,默认False**

​	**如果为True，则就地进行排序**

**⑤kind：{'quicksort', 'mergesort', 'heapsort', 'stable'}**

​	**排序算法的选择**

**⑥na_position: {'first', 'last'}， 默认'last'**

​	**如果为first，则把NaN放在开头，否则放在结尾，此参数在多级索引上未实现**

**⑦sort_remaining：bool, 默认True**

​	**当排序索引是多级时，即使指定了排序的level，则也会给其他层级索引进行排序**

**⑧ignore_index：bool, 默认False**

​	**如果为True，则结果轴将被标记为`0, 1, ..., n - 1`，否则保留原索引**

**⑨key：callable，可选**

​	**如果不为None，则在排序之前将key函数应用于索引值，这与`sorted()`里面的key参数类似，但显著的区别是此函数应该被向量化，它应该接收`Index`并返回相同形状的`Index`。对于多级索引，key按层级应用**



| 返回值： |
| -------- |

**:arrow_right:DataFrame或None**

​	**如果`inplace = True`的话会返回None，其他情况返回DataFrame**





**:a:对Series做操作**

```python
------------------------------------------------------------------------
s = pd.Series(['a', 'b', 'c', 'd', 'e'], index=[3, 2, 1, 4, np.nan])
print("=================原Series==================")
print(s)
print("=================对Series的索引进行排序，默认升序==================")
print(s.sort_index())
print("=================对Series的索引进行排序，指定降序排列，ascending=False==================")
print(s.sort_index(ascending=False))
print("=================对Series的索引进行升序排序，缺失值放在最上面==================")
print(s.sort_index(na_position='first'))
print("=================对Series的索引进行排序，忽略原先的索引值，使用0 —— n-1作为索引==================")
print(s.sort_index(ignore_index=True))
print("=================对Series就地排序，返回None==================")
print(s.sort_index(inplace=True))
print("=================再来看原Series，会发生改变==================")
print(s)
print("=================对Series的每个索引都执行key函数，之后根据得到的值进行排序==================")
print(s.sort_index(key=lambda x: np.exp(-x)))


#输出结果如下
=================原Series==================
3.0    a
2.0    b
1.0    c
4.0    d
NaN    e
dtype: object
=================对Series的索引进行排序，默认升序==================
1.0    c
2.0    b
3.0    a
4.0    d
NaN    e
dtype: object
=================对Series的索引进行排序，指定降序排列，ascending=False==================
4.0    d
3.0    a
2.0    b
1.0    c
NaN    e
dtype: object
=================对Series的索引进行升序排序，缺失值放在最上面==================
NaN    e
1.0    c
2.0    b
3.0    a
4.0    d
dtype: object
=================对Series的索引进行排序，忽略原先的索引值，使用0 —— n-1作为索引==================
0    c
1    b
2    a
3    d
4    e
dtype: object
=================对Series就地排序，返回None==================
None
=================再来看原Series，会发生改变==================
1.0    c
2.0    b
3.0    a
4.0    d
NaN    e
dtype: object
=================对Series的每个索引都执行key函数，之后根据得到的值进行排序==================
4.0    d
3.0    a
2.0    b
1.0    c
NaN    e
dtype: object
```



**:b:对DataFrame做操作**

```python
------------------------------------------------------------------------
df = pd.DataFrame(np.random.randint(25, size=(3, 4)),
                  index=[2, 6, 5],
                  columns=[2, 4, 1, 3])
print("=================原DataFrame==================")
print(df)
print("=================对DataFrame的行索引进行排序，默认升序==================")
print(df.sort_index())
print("=================对DataFrame列标签进行排序，默认升序==================")
print(df.sort_index(axis='columns'))
print("=================对DataFrame列标签进行排序，指定降序==================")
print(df.sort_index(axis='columns', ascending=False))
print("=================对DataFrame列标签进行排序，忽略原有的索引，使用 0—— n-1 ==================")
print(df.sort_index(axis='columns', ignore_index=True))
print("=================对DataFrame行索引就地排序，返回None==================")
print(df.sort_index(inplace=True))
print("=================再来看原DataFrame，会发生改变==================")
print(df)


#输出结果如下
=================原DataFrame==================
    2  4   1  3
2  16  0  15  4
6  10  0   0  9
5   9  7   5  0
=================对DataFrame的行索引进行排序，默认升序==================
    2  4   1  3
2  16  0  15  4
5   9  7   5  0
6  10  0   0  9
=================对DataFrame列标签进行排序，默认升序==================
    1   2  3  4
2  15  16  4  0
6   0  10  9  0
5   5   9  0  7
=================对DataFrame列标签进行排序，指定降序==================
   4  3   2   1
2  0  4  16  15
6  0  9  10   0
5  7  0   9   5
=================对DataFrame列标签进行排序，忽略原有的索引，使用 0—— n-1 ==================
    0   1  2  3
2  15  16  4  0
6   0  10  9  0
5   5   9  0  7
=================对DataFrame行索引就地排序，返回None==================
None
=================再来看原DataFrame，会发生改变==================
    2  4   1  3
2  16  0  15  4
5   9  7   5  0
6  10  0   0  9


#key参数应用于DataFrame的单独例子
----------------------------------------------------------
df = pd.DataFrame({"a": [1, 2, 3, 4]}, index=['A', 'b', 'C', 'd'])

>>> df.sort_index()		#这里因为在ASCII编码中，大写的字母在小写的字母之前，所以大写AC在小写bd之前
   a
A  1
C  3
b  2
d  4

#都转成小写在进行排序
>>> df.sort_index(key=lambda x: x.str.lower())
   a
A  1
b  2
C  3
d  4
```







### Series/DataFrame.sort_values

**==Series/DataFrame.sort_values(*by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None*)==**

​	**对于DataFrame，沿着某一个轴对值进行排序，对于Series，仅对值排序**



| 参数： |
| ------ |

**①by：str 或 str列表**

​	**指定要排序的行/列索引的名称**

- **如果 `axis= 0`或`axis = 'index'`，则要选择包含列标签的名称列表**
- **如果 `axis = 1`或`axis = 'columns'`，则要选择包含行索引的名称列表**

**②axis：{0 或 'index'，1 或 'columns'}，默认轴0**

​	**要沿哪个轴排序**

**③ascending：bool 或 布尔值列表，默认为True**

​	**按升序或降序排序。当索引为多级索引时，可以单独控制每个级别的排序方向**

**④inplace: bool,默认False**

​	**如果为True，则就地进行排序**

**⑤kind：{'quicksort', 'mergesort', 'heapsort', 'stable'}**

​	**排序算法的选择**

**⑥na_position: {'first', 'last'}， 默认'last'**

​	**如果为first，则把NaN放在开头，否则放在结尾，此参数在多级索引上未实现**

**⑦ignore_index：bool, 默认False**

​	**如果为True，则结果轴将被标记为`0, 1, ..., n - 1`，否则保留原索引**

**⑧key：callable，可选**

​	**如果不为None，则在排序之前将key函数应用于索引值，这与`sorted()`里面的key参数类似，但显著的区别是此函数应该被向量化，它应该接收`Index`并返回相同形状的`Index`。对于多级索引，key按层级应用**



**:a:对Series做操作**

```python
------------------------------------------------------------------------
s = pd.Series([-4, 1, 0, -2, 5], index=[5, 6, 1, 2, 7])
print("=================原Series==================")
print(s)
print("=================对Series中的值进行升序排序==================")
print(s.sort_values())
print("=================对Series中的值进行降序排序==================")
print(s.sort_values(ascending=False))
print("=================对Series中的值进行升序排序，并忽略原Series的索引==================")
print(s.sort_values(ignore_index=True))
print("=================对Series中的值应用sin(x)函数之后再排序==================")
print(s.sort_values(key=lambda x: np.sin(x)))
print("=================对Series中的值进行就地排序，返回None==================")
print(s.sort_values(inplace=True))
print("=================再看原来的Series，会发生改变==================")
print(s)
print("=================把Series中标签为5对应的值改成nan==================")
s.loc[5] = np.nan
print(s)
print("=================把Series中标签为5对应的值改成nan，再排序，缺失值在最后==================")
print(s.sort_values())
print("=================把Series中标签为5对应的值改成nan，再排序，指定缺失值在最前面==================")
print(s.sort_values(na_position='first'))


=================原Series==================
5   -4
6    1
1    0
2   -2
7    5
dtype: int64
=================对Series中的值进行升序排序==================
5   -4
2   -2
1    0
6    1
7    5
dtype: int64
=================对Series中的值进行降序排序==================
7    5
6    1
1    0
2   -2
5   -4
dtype: int64
=================对Series中的值进行升序排序，并忽略原Series的索引==================
0   -4
1   -2
2    0
3    1
4    5
dtype: int64
=================对Series中的值应用sin(x)函数之后再排序==================
7    5
2   -2
1    0
5   -4
6    1
dtype: int64
=================对Series中的值进行就地排序，返回None==================
None
=================再看原来的Series，会发生改变==================
5   -4
2   -2
1    0
6    1
7    5
dtype: int64
=================把Series中标签为5对应的值改成nan==================
5    NaN
2   -2.0
1    0.0
6    1.0
7    5.0
dtype: float64
=================把Series中标签为5对应的值改成nan，再排序，缺失值在最后==================
2   -2.0
1    0.0
6    1.0
7    5.0
5    NaN
dtype: float64
=================把Series中标签为5对应的值改成nan，再排序，指定缺失值在最前面==================
5    NaN
2   -2.0
1    0.0
6    1.0
7    5.0
dtype: float64
```





**:b:对DataFrame做操作**

```python
#第一个例子
------------------------------------------------------------------------
df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})
print("=================原DataFrame==================")
print(df)
print("=================指定对DataFrame的col1进行排序==================")
print(df.sort_values(by=['col1']))
print("=================指定对DataFrame的col1和col2进行排序==================")
print(df.sort_values(by=['col1', 'col2']))
print("=================指定对DataFrame的col1进行排序,缺失值放到第一个==================")
print(df.sort_values(by=['col1'], na_position='first'))



#输出结果如下
=================原DataFrame==================
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
=================指定对DataFrame的col1进行排序==================
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D
=================指定对DataFrame的col1和col2进行排序==================
  col1  col2  col3 col4
1    A     1     1    B
0    A     2     0    a
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D
=================指定对DataFrame的col1进行排序,缺失值放到第一个==================
  col1  col2  col3 col4
3  NaN     8     4    D
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e




#第二个例子
------------------------------------------------------------------------
df = pd.DataFrame(np.random.randint(25, size=(3, 4)),
                  index=[2, 6, 5],
                  columns=[2, 4, 1, 3])
print("=================原DataFrame==================")
print(df)
print("=================对DataFrame的列标签为2的列进行排序，默认升序==================")
print(df.sort_values(2))
print("=================对DataFrame中列标签为2的列中的值应用sin(x)函数,之后再进行排序==================")
print(df.sort_values(2, key=lambda x: np.sin(x)))
print("=================对DataFrame列标签为2的列进行排序，忽略原有的索引，使用 0 —— n-1 ==================")
print(df.sort_values(2, ignore_index=True))
print("=================对DataFrame行标签为6的行的值进行排序，默认升序==================")
print(df.sort_values(6, axis='columns'))
print("=================对DataFrame行标签为6和5的行进行排序，先排6再排5，指定降序==================")
print(df.sort_values([6, 5], axis='columns', ascending=False))
print("=================对DataFrame的列标签为2的列进行就地排序，返回None==================")
print(df.sort_values(2, inplace=True))
print("=================再来看原DataFrame，会发生改变==================")
print(df)



#输出结果如下
=================原DataFrame==================
    2   4   1  3
2  16  14  11  0
6  13   8  18  6
5  14  11  17  0
=================对DataFrame的列标签为2的列进行排序，默认升序==================
    2   4   1  3
6  13   8  18  6
5  14  11  17  0
2  16  14  11  0
=================对DataFrame中列标签为2的列中的值应用sin(x)函数,之后再进行排序==================
    2   4   1  3
2  16  14  11  0
6  13   8  18  6
5  14  11  17  0
=================对DataFrame列标签为2的列进行排序，忽略原有的索引，使用 0 —— n-1 ==================
    2   4   1  3
0  13   8  18  6
1  14  11  17  0
2  16  14  11  0
=================对DataFrame行标签为6的行的值进行排序，默认升序==================
   3   4   2   1
2  0  14  16  11
6  6   8  13  18
5  0  11  14  17
=================对DataFrame行标签为6和5的行进行排序，先排6再排5，指定降序==================
    1   2   4  3
2  11  16  14  0
6  18  13   8  6
5  17  14  11  0
=================对DataFrame的列标签为2的列进行就地排序，返回None==================
None
=================再来看原DataFrame，会发生改变==================
    2   4   1  3
6  13   8  18  6
5  14  11  17  0
2  16  14  11  0
```





### Series/DataFrame.rank

**==Series/DataFrame.rank(*axis=0, method='average', numeric_only=False, na_option='keep', ascending=True, pct=False*)==**

​	**沿某个轴计算数值的排名。默认情况下，为相等的值分配一个排名，该排名是这些值排名的平均值**



| 参数： |
| ------ |

**①axis: {0 或 'index', 1 或 'columns'}，默认0**

​	**要沿哪个轴进行排名**

**②method：{'average', 'min', 'max', 'first', 'dense'}, 默认'average'**

​	**如何对具有相同排名元素的记录组进行排名**

- **'average'：使用组内平均值排名**
- **'min'：使用组中的最低排名**
- **'max'：使用组中的最高排名**
- **'first'：按组中出现的顺序排名**
- **'dense'：类似于'min'，但组之间的排名总是加1**

**③numeric_only：bool, 默认False**

​	**对于DataFrame对象，如果设置为True，则仅对数字列进行排名**

**④na_option: {'keep', 'top', 'bottom'}, 默认'keep'**

​	**如何对NaN进行排序**

- **'keep'：为NaN值分配排名**
- **'top'：把NaN排到最前面**
- **'bottom'：把NaN排到最后面**

**⑤ascending：bool，默认为True**

​	**是否按升序排列**

**⑥pct：bool, 默认False**

​	**是否以百分位数形式显示排名**



| 返回值： |
| -------- |

**:arrow_right:返回与调用者类型相同的排名信息**





**:a:Series操作**

```python
s = pd.Series([0, 1, 2, 3, 2, np.nan], index=list('abcdef'))
print("=================原Series==================")
print(s)
print("=================计算Series中元素的排名==================")
print("=================如果存在并列排名的元素，则把它们当成一组，使用组内排名的平均值排名==================")
print(s.rank())
print("=================计算Series中元素的排名，method='min',使用并列排名组的最小值排名==================")
print(s.rank(method='min'))
print("=================计算Series中元素的排名，method='max',使用并列排名组的最大值排名==================")
print(s.rank(method='max'))
print("=================计算Series中元素的排名，method='first',并列元素的排名按Series中元素出现的顺序排名==================")
print(s.rank(method='first'))
print("=================计算Series中元素的排名，method='dense',类似于最小值排名，但组之间的排名+1==================")
print(s.rank(method='dense'))
print("=================计算Series中元素的排名，把缺失值排到最上面==================")
print(s.rank(na_option='top'))
print("=================计算Series中元素的排名，把缺失值排到最下面==================")
print(s.rank(na_option='bottom'))
print("=================计算Series中元素的排名，指定降序排序==================")
print(s.rank(ascending=False))
print("=================计算Series中元素的排名，使用百分比==================")
print(s.rank(pct=True))


#输出结果如下
=================原Series==================
a    0.0
b    1.0
c    2.0
d    3.0
e    2.0
f    NaN
dtype: float64
=================计算Series中元素的排名==================
=================如果存在并列排名的元素，则把它们当成一组，使用组内排名的平均值排名==================
a    1.0
b    2.0
c    3.5			#(3+4)/2 = 3.5
d    5.0
e    3.5
f    NaN
dtype: float64
=================计算Series中元素的排名，method='min',使用并列排名组的最小值排名==================
a    1.0
b    2.0
c    3.0
d    5.0
e    3.0
f    NaN
dtype: float64
=================计算Series中元素的排名，method='max',使用并列排名组的最大值排名==================
a    1.0
b    2.0
c    4.0
d    5.0
e    4.0
f    NaN
dtype: float64
=================计算Series中元素的排名，method='first',并列元素的排名按Series中元素出现的顺序排名==================
a    1.0
b    2.0
c    3.0
d    5.0
e    4.0
f    NaN
dtype: float64
=================计算Series中元素的排名，method='dense',类似于最小值排名，但组之间的排名+1==================
a    1.0
b    2.0
c    3.0
d    4.0
e    3.0
f    NaN
dtype: float64
=================计算Series中元素的排名，把缺失值排到最上面==================
a    2.0
b    3.0
c    4.5
d    6.0
e    4.5
f    1.0				#NaN被排到了第一个
dtype: float64
=================计算Series中元素的排名，把缺失值排到最下面==================
a    1.0
b    2.0
c    3.5
d    5.0
e    3.5
f    6.0				#NaN被排到了最后一个
dtype: float64
=================计算Series中元素的排名，指定降序排序==================
a    5.0
b    4.0
c    2.5
d    1.0
e    2.5
f    NaN
dtype: float64
=================计算Series中元素的排名，使用百分比==================
a    0.2
b    0.4
c    0.7
d    1.0
e    0.7
f    NaN
dtype: float64
```



**:b:DataFrame操作**

```python
np.random.seed(15)
df = pd.DataFrame(np.random.randint(25, size=(3, 4)),
                  index=[2, 6, 5],
                  columns=[2, 4, 1, 3])
print("=================原DataFrame==================")
print(df)
print("=================对DataFrame的所有列进行排序==================")
print(df.rank())
print("=================对DataFrame的所有行进行排序==================")
print(df.rank(axis='columns'))
print("=================对DataFrame行标签对6的行进行排序==================")
df.loc["axis_1_loc6"] = df.loc[6].rank()
print(df)
print("=================对DataFrame列标签为4的列进行排序==================")
df["rank"] = df[4].rank()
df["ascending_false"] = df[4].rank(ascending=False)
df["pct"] = df[4].rank(pct=True)
print(df)
df = pd.DataFrame(np.random.randint(25, size=(3, 4)),
                  index=[2, 6, 5],
                  columns=[2, 4, 1, 3])
print("=================对DataFrame列标签为4的列进行排序，method参数==================")
df.loc[6, 4] = df.loc[5, 4]
df["method_min"] = df[4].rank(method='min')
df["method_max"] = df[4].rank(method='max')
df["method_first"] = df[4].rank(method='first')
df["method_dense"] = df[4].rank(method='dense')
print(df)


#输出结果如下
=================原DataFrame==================
    2   4   1   3
2   8  21  12   5
6  23   0   7  11
5  21  22  15  17
=================对DataFrame的所有列进行排序==================
     2    4    1    3
2  1.0  2.0  2.0  1.0
6  3.0  1.0  1.0  2.0
5  2.0  3.0  3.0  3.0
=================对DataFrame的所有行进行排序==================
     2    4    1    3
2  2.0  4.0  3.0  1.0
6  4.0  1.0  2.0  3.0
5  3.0  4.0  1.0  2.0
=================对DataFrame行标签对6的行进行排序==================
                2     4     1     3
2             8.0  21.0  12.0   5.0
6            23.0   0.0   7.0  11.0
5            21.0  22.0  15.0  17.0
axis_1_loc6   4.0   1.0   2.0   3.0
=================对DataFrame列标签为4的列进行排序==================
                2     4     1     3  rank  ascending_false   pct
2             8.0  21.0  12.0   5.0   3.0              2.0  0.75
6            23.0   0.0   7.0  11.0   1.0              4.0  0.25
5            21.0  22.0  15.0  17.0   4.0              1.0  1.00
axis_1_loc6   4.0   1.0   2.0   3.0   2.0              3.0  0.50
=================对DataFrame列标签为4的列进行排序，method参数==================
    2   4   1   3  method_min  method_max  method_first  method_dense
2  13  23   0  10         3.0         3.0           3.0           2.0
6  15  19   9   7         1.0         2.0           1.0           1.0
5   5  19  12  13         1.0         2.0           2.0           1.0
```





### Series/DataFrame.take

**==Series/DataFrame.take(*indices, axis=0, \*\*kwargs*)==**

​	**返回沿某个轴给定位置索引的元素，这意味着我们不是根据对象的index属性中的实际值进行索引，而是根据元素在对象中的实际位置进行索引。**



| 参数： |
| ------ |

**①indices：array_like**

​	**指定要获取哪些位置的数据，这些位置表示元素在对象中的实际位置，并不是索引，其位置由一个数组给出，可以是负整数的数组。例如`take([1, 2])`代表获取对象中第一个和第二个位置的数据，而不是索引/标签为`1,2`的数据。**

**②axis：{0 或 'index', 1 或 'columns'， None}，默认0**

​	**要沿哪个轴选择数据**

**③\*\*kwargs**

​	**其他关键字参数，以适配`numpy.take()`**



| 返回值： |
| -------- |

**:arrow_right:与调用者类型相同的对象**



```python
df = pd.DataFrame([('falcon', 'bird', 389.0),
                   ('parrot', 'bird', 24.0),
                   ('lion', 'mammal', 80.5),
                   ('monkey', 'mammal', np.nan)],
                  columns=['name', 'class', 'max_speed'],
                  index=[0, 2, 3, 1])
print("============原DataFrame===============")
print(df)
print("===============选取第二行和第三行的数据 [1, 2]====================")
print(df.take([1, 2]))
print("===============选取第第二列和第三列的数据，[1, 2] axis = columns====================")
print(df.take([1, 2], axis='columns'))
print("===============选取倒数第一行和倒数第三行的数据 [-1, -3]====================")
print(df.take([-1, -3]))



#输出结果如下
============原DataFrame===============
     name   class  max_speed
0  falcon    bird      389.0
2  parrot    bird       24.0
3    lion  mammal       80.5
1  monkey  mammal        NaN
===============选取第二行和第三行的数据 [1, 2]====================
     name   class  max_speed
2  parrot    bird       24.0
3    lion  mammal       80.5
===============选取第第二列和第三列的数据，[1, 2] axis = columns====================
    class  max_speed
0    bird      389.0
2    bird       24.0
3  mammal       80.5
1  mammal        NaN
===============选取倒数第一行和倒数第三行的数据 [-1, -3]====================
     name   class  max_speed
1  monkey  mammal        NaN
2  parrot    bird       24.0
```







## # 二元运算符函数

|              方法              |                             说明                             |
| :----------------------------: | :----------------------------------------------------------: |
|           `add/radd`           |                             $+$                              |
|           `sub/rsub`           |                             $-$                              |
|           `mul/rmul`           |                           $\times$                           |
| `div/rdiv`或`truediv/rtruediv` |                             除法                             |
|      `floordiv/rfloordiv`      |                           $a // b$                           |
|           `mod/rmod`           |                            $a\%b$                            |
|           `pow/rpow`           |                            幂运算                            |
|             `dot`              |              计算DataFrame和其他数据的矩阵乘法               |
|      `lt/gt/le/ge/ne/eq`       | $\lt 、\gt、\le、\ge 、\ne、= $<br />逐个元素比较返回布尔值的DataFrame |



### 1、DataFrame调用

**参数列表：==*other, axis='columns', level=None, fill_value=None*==**

| 参数： |
| ------ |

**①other：标量，序列，Series，dict或DataFrame**

​	**要与DataFrame进行操作的对象**

**②axis：{0或'index'， 1或'columns'}**

​	**沿着哪个轴进行操作，默认沿着列标签进行，即`axis='columns'`**

**③level：int或标签**

​	**跨级别广播，匹配传递的 MultiIndex 级别上的索引值**

**④fill_value：float或None，默认为None**

​	**在计算之前，用此值填充现有的缺失值。**



#### :one:**other =  标量** ####

```python
df = pd.DataFrame({'angles': [0, 3, 4],
                   'degrees': [360, 180, 360]},
                  index=['circle', 'triangle', 'rectangle'])
print("========原DataFrame========")
print(df)
print("================通过add函数，DataFrame的每个元素加10==================")
print(df.add(10))
print("================通过+号，DataFrame的每个元素加1==================")
print(df + 1)
print("================df - 5==================")
print(df.sub(5))
print("================5 - df==================")
print(df.rsub(5))
print("================df * 5==================")
print(df.mul(5))
print("================df / 10==================")
print(df.div(10))
print("================df / 10==================")
print(df.truediv(10))
print("================10 / df==================")
print(df.rdiv(10))
print("================df // 10==================")
print(df.floordiv(10))
print("================df ** 2==================")
print(df.pow(2))
print("================df < 10==================")
print(df.lt(10))


#输出结果如下
========原DataFrame========
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360
================通过add函数，DataFrame的每个元素加10==================
           angles  degrees
circle         10      370
triangle       13      190
rectangle      14      370
================通过+号，DataFrame的每个元素加1==================
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361
================df - 5==================
           angles  degrees
circle         -5      355
triangle       -2      175
rectangle      -1      355
================5 - df==================
           angles  degrees
circle          5     -355
triangle        2     -175
rectangle       1     -355
================df * 5==================
           angles  degrees
circle          0     1800
triangle       15      900
rectangle      20     1800
================df / 10==================
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0
================df / 10==================
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0
================10 / df==================
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778
================df // 10==================
           angles  degrees
circle          0       36
triangle        0       18
rectangle       0       36
================df ** 2==================
           angles  degrees
circle          0   129600
triangle        9    32400
rectangle      16   129600
================df < 10==================
           angles  degrees
circle       True    False
triangle     True    False
rectangle    True    False

```



#### **:two:other = 序列** ####

​	**这种情况下，传入的序列的长度要和指定轴标签的数量相同，否则会引发异常**

```python
df = pd.DataFrame({'angles': [0, 3, 4],
                   'degrees': [360, 180, 360]},
                  index=['circle', 'triangle', 'rectangle'])
print("==================原DataFrame========================")
print(df)
print("==================默认对每一列做操作，第一列 - 1 ，第二列 - 2========================")
print(df.sub([1, 2]))
print("==================指定对每一列做操作，第一列 - 1 ，第二列 - 2========================")
print(df.sub([1, 2], axis='columns'))
print("==================指定对每一行做操作，第一行- 2 ，第二行 - 5 ， 第三行 - 3========================")
print(df.sub([2, 5, 3], axis='index'))
print("==================默认对每一列做操作，第一列不等于3的值为True ，第二列不等于180的为True========================")
print(df.ne([3, 180]))
print("==================指定对每一行做操作，第一行不等于0的值为True ，第二行不等于3的为True，第三行不等于180的为True========================")
print(df.ne([0, 3, 180], axis='index'))



#输出结果如下
==================原DataFrame========================
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360
==================默认对每一列做操作，第一列 - 1 ，第二列 - 2========================
           angles  degrees
circle         -1      358
triangle        2      178
rectangle       3      358
==================指定对每一列做操作，第一列 - 1 ，第二列 - 2========================
           angles  degrees
circle         -1      358
triangle        2      178
rectangle       3      358
==================指定对每一行做操作，第一行- 2 ，第二行 - 5 ， 第三行 - 3========================
           angles  degrees
circle         -2      358
triangle       -2      175
rectangle       1      357
==================默认对每一列做操作，第一列不等于3的值为True ，第二列不等于180的为True========================
           angles  degrees
circle       True     True
triangle    False    False
rectangle    True     True
==================指定对每一行做操作，第一行不等于0的值为True ，第二行不等于3的为True，第三行不等于180的为True========================
           angles  degrees
circle      False     True
triangle    False     True
rectangle    True     True

```





#### **:three:other = Series** ####

​	**此情况下，传入的Series的长度要和DataFrame的指定轴标签的长度相同，并且要和标签对齐才会做运算。**

​	**对于无法对齐的标签，会新增此标签，并把标签相应的行/列设为`NaN`**

```python
df = pd.DataFrame({'angles': [0, 3, 4],
                   'degrees': [360, 180, 360]},
                  index=['circle', 'triangle', 'rectangle'])
print("==================原DataFrame========================")
print(df)
print("==================Series1========================")
ser1 = pd.Series([1, 2], index=['angles', 'degrees'])
print(ser1)
print("==================Series2========================")
ser2 = pd.Series([1, 2, 3, 4], index=['circle', 'triangle', 'rectangle', 'square'])
print(ser2)
print("================== 默认对列操作，DataFrame的每一列 - Series1的每个元素========================")
print(df.sub(ser1))
print("==================指定对列操作，DataFrame的每一列 + Series1的每个元素========================")
print(df.add(ser1, axis='columns'))
print("==================指定对行操作，DataFrame的每一行 + Series2的每个元素========================")
print(df.add(ser2, axis='index'))
print("==================指定对行操作，DataFrame的每一行 * Series2的每个元素========================")
print(df.mul(ser2, axis='index'))
print("==================默认对列操作，DataFrame的每一列 >= Series2的每个元素，则返回True========================")
print(df.ge(pd.Series([3, 181], index=["angles", "degrees"])))


#输出结果如下
==================原DataFrame========================
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360
==================Series1========================
angles     1
degrees    2
dtype: int64
==================Series2========================
circle       1
triangle     2
rectangle    3
square       4
dtype: int64
================== 默认对列操作，DataFrame的每一列 - Series1的每个元素========================
           angles  degrees
circle         -1      358
triangle        2      178
rectangle       3      358
==================指定对列操作，DataFrame的每一列 + Series1的每个元素========================
           angles  degrees
circle          1      362
triangle        4      182
rectangle       5      362
==================指定对行操作，DataFrame的每一行 + Series2的每个元素========================
           angles  degrees
circle        1.0    361.0
rectangle     7.0    363.0
square        NaN      NaN
triangle      5.0    182.0
==================指定对行操作，DataFrame的每一行 * Series2的每个元素========================
           angles  degrees
circle        0.0    360.0
rectangle    12.0   1080.0
square        NaN      NaN
triangle      6.0    360.0
==================默认对列操作，DataFrame的每一列 >= Series2的每个元素，则返回True========================
           angles  degrees
circle      False     True
triangle     True    False
rectangle    True     True

```



#### **:four:other = dict** ####

​	**此种情况下，字典的项数必须等于DataFrame的行/列标签的数量，否则会报错[ValueError: Unable to coerce to Series][]**

​	**这时，字典的键和DataFrame的行/列标签进行对齐，字典的值和DataFrame中相对应的值做运算。**

​	**如果存在标签无法对齐的情况，则会把该标签对应的数据设为`NaN`**

```python
df = pd.DataFrame({'angles': [0, 3, 4],
                   'degrees': [360, 180, 360]},
                  index=['circle', 'triangle', 'rectangle'])

#默认和列标签做运算，进行标签对齐
>>> df.mul({'angles': 0, 'degrees': 2})
            angles  degrees
circle           0      720
triangle         0      360
rectangle        0      720


#指定和行做运算，进行标签对齐
>>> df.mul({'circle': 0, 'triangle': 2, 'rectangle': 3}, axis='index')
            angles  degrees
circle           0        0
triangle         6      360
rectangle       12     1080


#标签 aaa 无法对齐， 所以为NaN
>>> df.mul({'angles': 0, 'aaa': 3})
           angles  degrees
circle        0.0      NaN
triangle      0.0      NaN
rectangle     0.0      NaN
```



#### **:five:other = DataFrame** ####

​	**此情况下，两个DataFrame会进行标签对齐做运算，如果有无法对齐的标签，则会设置为`NaN`。**

​	**此时，使用`fill_value`参数会设置无法对齐标签对应的值**

```python
print("==================原DataFrame========================")
print(df)
other = pd.DataFrame({'angles': [0, 3, 4]},
                     index=['circle', 'triangle', 'rectangle'])
print("==================要传入的DataFrame========================")
print(other)
print("==================进行标签对齐，两个df的数据做乘法========================")
print(df * other)
print("==================进行标签对齐，两个df的数据做乘法，把other中无法对齐标签的NaN填充为5========================")
print(df.mul(other, fill_value=3))


#输出结果如下
==================原DataFrame========================
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360
==================要传入的DataFrame========================
           angles
circle          0
triangle        3
rectangle       4
==================进行标签对齐，两个df的数据做乘法========================
           angles  degrees
circle          0      NaN
triangle        9      NaN
rectangle      16      NaN
==================进行标签对齐，两个df的数据做乘法，把other中无法对齐标签的NaN填充为5========================
           angles  degrees
circle          0   1080.0
triangle        9    540.0
rectangle      16   1080.0

```





### 2、Series调用

**参数列表：==*other, level=None, fill_value=None, axis=0*==**

| 参数： |
| ------ |

**①other：Series或标量**

**②level：int或name**

​	**跨级别广播，匹配传递的 MultiIndex 级别上的索引值**

**③fill_value：None或浮点数，默认为None**

​	**在计算之前，使用此值填充现有的缺失值**

**④aixs: {0 或 'index'}**



#### **:one:other = 标量** ####

```python
indexs = list("apple")
ser = pd.Series([0, 1, 2, np.nan, 4], index=indexs, name='integer')
print("=========原Series===========")
print(ser)
print("=========Series的每个元素加1===========")
print(ser.add(1))
print("=========把Series中的nan填充为5之后，Series的每个元素加1，===========")
print(ser.add(1, fill_value=5))


#运行结果如下
=========原Series===========
a    0.0
p    1.0
p    2.0
l    NaN
e    4.0
Name: integer, dtype: float64
=========Series的每个元素加1===========
a    1.0
p    2.0
p    3.0
l    NaN
e    5.0
Name: integer, dtype: float64
=========把Series中的nan填充为5之后，Series的每个元素加1，===========
a    1.0
p    2.0
p    3.0
l    6.0
e    5.0
Name: integer, dtype: float64

```





#### **:two:other = Series** ####

```python
indexs = list("apple")
ser = pd.Series([0, 1, 2, np.nan, 4], index=indexs, name='integer')
ser1 = pd.Series([0, np.nan, 3, 5, np.nan], index=indexs)
print("=========第一个Series===========")
print(ser)
print("=========第二个Series===========")
print(ser1)
print("=========把两个Series的nan都填充为0，之后两个Series相加，标签对齐===========")
print(ser.add(ser1, fill_value=0))


#运行结果如下
=========第一个Series===========
a    0.0
p    1.0
p    2.0
l    NaN
e    4.0
Name: integer, dtype: float64
=========第二个Series===========
a    0.0
p    NaN
p    3.0
l    5.0
e    NaN
dtype: float64
=========把两个Series的nan都填充为0，之后两个Series相加，标签对齐===========
a    0.0
p    1.0
p    5.0
l    5.0
e    4.0
dtype: float64

```









## # 统计

|       方法       |                        说明                         |
| :--------------: | :-------------------------------------------------: |
|     `count`      |                  计算非NA值的数量                   |
|    `describe`    |                  计算汇总统计信息                   |
|    `min/max`     |                   最大值和最小值                    |
| `argmin/argmax`  | 最大值和最小值的整数索引位置，DataFrame对象上不可用 |
| `idxmin/idxmax`  |              最大值和最小值的索引标签               |
|    `quantile`    |       计算样本 0—1 之间的分位数（默认为0.5）        |
|      `sum`       |                    所有值的总和                     |
|      `mean`      |                   所有值的平均数                    |
|     `median`     |           所有值的算术中位数（50%分位数）           |
| `cumsum/cumprod` |               所有值的累加和/累积乘积               |
| `cummin/cummax`  |             所有值的累计最大值和最小值              |
|      `mad`       |                平均值的平均绝对偏差                 |
|      `var`       |                   样本无偏的方差                    |
|      `std`       |                     样本标准差                      |
|      `corr`      |       返回相关系数矩阵（每列两两的相关系数）        |
|    `corrwith`    |                   计算成对相关性                    |
|      `cov`       |                   返回协方差矩阵                    |
|      `diff`      |          计算一阶差分（对时间序列很有用）           |
|      `skew`      |              样本无偏的偏度（三阶矩）               |
|      `kurt`      |            返回样本的无偏峰度（四阶矩）             |
|   `pct_change`   |         返回当前元素和之前元素的百分比变化          |
|  `value_counts`  |                      频次统计                       |



### Series/DataFrame.describe

**==DataFrame.describe(*percentiles=None, include=None, exclude=None*)==**

​	**生成描述性统计数据，统计数据包括数据集的集中趋势、离散度和形状的统计数据**



| 参数： |
| ------ |

**①percentiles：数字列表，可选**

​	**要包含在输出中的百分位数，百分位数介于0-1之间，默认值为`[0.25, 0.5, 0.75]`**

**②include："all", dtypes的列表或None，可选**

​	**要在结果中囊括的数据类型**

**③exclude：dtypes列表或None，可选**

​	**要从结果中忽略的数据类型**



| 返回值： |
| -------- |

**:arrow_right:Series或DataFrame**

​	**Series或DataFrame的总体描述**



**:heavy_exclamation_mark:注意以下几点**

- **对于数值型的数据，结果的索引包括`count`,`mean`,`std`,`min`,`max`以及`[0.25,0.5,0.75]`分位数**
- **对于对象数据（例如字符串或时间戳），结果的索引包括`count`,`unique`,`top`,`freq`。时间戳还包括`first`和`last`两项。其中，`unique`为数据中未重复元素的个数，`top`是出现次数最多的元素，`freq`是出现次数最多的元素出现的次数**





```python
#Series调用
-----------------------------------------------------------------------------
print("===========整数序列=============")
num_ser = pd.Series(np.arange(4))
print(num_ser.describe())
print("===========字符串序列=============")
str_ser = pd.Series(list("apple"), name='s')
print(str_ser.describe())
print("===========时间戳序列 Timestamp对象包含int64位整数值=============")
date_ser = pd.Series([
    np.datetime64("2000-01-01"),
    np.datetime64("2010-01-01"),
    np.datetime64("2010-01-01")
])
print(date_ser.describe())


#输出结果如下
===========整数序列=============
count    4.000000
mean     1.500000
std      1.290994
min      0.000000
25%      0.750000
50%      1.500000
75%      2.250000
max      3.000000
dtype: float64
===========字符串序列=============
count     5
unique    4
top       p
freq      2
Name: s, dtype: object
===========时间戳序列 Timestamp对象包含int64位整数值=============
count                      3
mean     2006-09-01 08:00:00
min      2000-01-01 00:00:00
25%      2004-12-31 12:00:00
50%      2010-01-01 00:00:00
75%      2010-01-01 00:00:00
max      2010-01-01 00:00:00
dtype: object


#DataFrame调用
-----------------------------------------------------------------------------
df = pd.DataFrame({'categorical': pd.Categorical(['d', 'e', 'f']),
                   'numeric': [1, 2, 3],
                   'object': ['a', 'b', 'c']
                   })
print("===========原DataFrame==============")
print(df)
print("===========混合数据类型的DataFrame，只返回数字列的信息==============")
print(df.describe())
print("===========包含DataFrame所有列的信息==============")
print(df.describe(include='all'))
print("===========包含DataFrame的object列的信息==============")
print(df.describe(include=['object']))
print("===========不包含DataFrame的object列的信息==============")
print(df.describe(exclude=['object']))
print("===========DataFrame的categorical列的信息==============")
print(df["categorical"].describe())


#输出结果如下
===========原DataFrame==============
  categorical  numeric object
0           d        1      a
1           e        2      b
2           f        3      c
===========混合数据类型的DataFrame，只返回数字列的信息==============
       numeric
count      3.0
mean       2.0
std        1.0
min        1.0
25%        1.5
50%        2.0
75%        2.5
max        3.0
===========包含DataFrame所有列的信息==============
       categorical  numeric object
count            3      3.0      3
unique           3      NaN      3
top              d      NaN      a
freq             1      NaN      1
mean           NaN      2.0    NaN
std            NaN      1.0    NaN
min            NaN      1.0    NaN
25%            NaN      1.5    NaN
50%            NaN      2.0    NaN
75%            NaN      2.5    NaN
max            NaN      3.0    NaN
===========包含DataFrame的object列的信息==============
       object
count       3
unique      3
top         a
freq        1
===========不包含DataFrame的object列的信息==============
       categorical  numeric
count            3      3.0
unique           3      NaN
top              d      NaN
freq             1      NaN
mean           NaN      2.0
std            NaN      1.0
min            NaN      1.0
25%            NaN      1.5
50%            NaN      2.0
75%            NaN      2.5
max            NaN      3.0
===========DataFrame的categorical列的信息==============
count     3
unique    3
top       d
freq      1
Name: categorical, dtype: object

```



### Series/DataFrame.idxmax/idxmin

**==Series/DataFrame.idxmax/idmin(*axis=0, skipna=True, numeric_only=False*)==**

​	**返回沿某个轴第一次出现最大值/最小值的索引，默认对列进行操作，此函数下，NA/null 值会被排除**

​	**此方法可以看成`ndarray.argmax/argmin`**



| 参数： |
| ------ |

**①axis：{0 或 'index' ，1 或 'columns'}， 默认为0**

​	**要沿哪个轴进行操作**

**②skipna：bool，默认为True**

​	**是否跳过NA/null，如果整行/列都是NA，则结果会是NA**

**③numeric_only：bool，默认False**

​	**是否只对数值型数据处理，数值型只包含浮点数、整型或布尔值数据**

​	**当调用对象是Series时，无此参数**



| 返回值： |
| -------- |

**:arrow_right:返回Series（调用者是DataFrame）或索引（调用者是Series）**



```python
#Series操作
-----------------------------------------------------------------
ser = pd.Series(data=[1, None, 4, 3, 4],
              index=['A', 'B', 'C', 'D', 'E'])
print(ser)
print(ser.idxmax())
print(ser.idxmin())

#运行结果如下
A    1.0
B    NaN
C    4.0
D    3.0
E    4.0
dtype: float64
C				#默认跳过nan，第一次出现最大值的标签/索引为 C
A				#最小值对应的索引为 A



#DataFrame操作
-----------------------------------------------------------------
df = pd.DataFrame({'consumption': [10.51, 103.11, 55.48],
                    'co2_emissions': [37.2, 19.66, 1712]},
                  index=['Pork', 'Wheat Products', 'Beef'])
print("==================原DataFrame========================")
print(df)
print("==================DataFrame每一列的最大值对应的索引========================")
print(df.idxmax(), type(df.idxmax()))
print("==================DataFrame每一行的最大值对应的列标签========================")
print(df.idxmax(axis='columns'), type(df.idxmax(axis='columns')))


#输出结果如下
==================原DataFrame========================
                consumption  co2_emissions
Pork                  10.51          37.20
Wheat Products       103.11          19.66
Beef                  55.48        1712.00
==================DataFrame每一列的最大值对应的索引========================
consumption      Wheat Products
co2_emissions              Beef
dtype: object <class 'pandas.core.series.Series'>
==================DataFrame每一行的最大值对应的列标签========================
Pork              co2_emissions
Wheat Products      consumption
Beef              co2_emissions
dtype: object <class 'pandas.core.series.Series'>

```





### Series/DataFrame.quantile

**==DataFrame.quantile(*q=0.5, axis=0*)==**

​	**沿着某个轴计算分位数的值，默认对每一列进行计算**



| 参数： |
| ------ |

**①q：float 或array_like，默认是0.5**

​	**$0 \le q \le 1$，表示要计算的分位数**

**②axis：{0 或 'index'，1 或 'columns'}，默认为0**

​	**沿着哪个轴进行操作**



| 返回值： |
| -------- |

**:arrow_right:Series或DataFrame**

​	**:a:如果`q`是一个float，则会返回一个序列，序列的索引是原DataFrame的列，值是分位数**

​	**:b:如果`q`是一个array，则返回DataFrame，其行标签为`q`中的每一个元素，列标签是原DataFrame的列/行，值是分位数**





```python
df = pd.DataFrame(np.array([[1, 1], [2, 10], [3, 100], [4, 100]]),
                  columns=['a', 'b'])
print("==================原DataFrame========================")
print(df)
print("==================对列进行操作，每一列计算0.2分位数，返回Series========================")
print(df.quantile(0.2))
print("==================对列进行操作，每一列计算对应的分位数，返回DataFrame========================")
print(df.quantile([0.1 , 0.25]))
print("==================对行进行操作，每一行计算对应的分位数，返回DataFrame========================")
print(df.quantile([0.1 , 0.25, 0.5, 0.75], axis='columns'))


#输出结果如下
==================原DataFrame========================
   a    b
0  1    1
1  2   10
2  3  100
3  4  100
==================对列进行操作，每一列计算0.2分位数，返回Series========================
a    1.6
b    6.4
Name: 0.2, dtype: float64
==================对列进行操作，每一列计算对应的分位数，返回DataFrame========================
         a     b
0.10  1.30  3.70
0.25  1.75  7.75
==================对行进行操作，每一行计算对应的分位数，返回DataFrame========================
        0    1      2     3
0.10  1.0  2.8  12.70  13.6
0.25  1.0  4.0  27.25  28.0
0.50  1.0  6.0  51.50  52.0
0.75  1.0  8.0  75.75  76.0

```



### Series.corr

**==Series.corr(*other, method='pearson', min_periods=None*)==**

​	**计算两个Series的相关系数，包括缺失值，两个Series的长度不需要相同（参考相关系数的定义）**



| 参数： |
| ------ |

**①other：Series**

​	**指定用哪一个Series用来计算相关系数，计算前需标签对齐，如果存在无法对齐的标签，则输出`nan`**

**②method：{'pearson', 'kendall', 'spearman'} 或 callable**

- **pearson：皮尔逊系数，标准相关系数**
- **kendall: 肯德尔系数**
- **spearman：斯皮尔曼等级相关**
- **callable：输入是两个一维ndarray的可调用对象（函数）**

**③min_periods：int，可选**

​	**每列的最小观测数，只适用于皮尔逊和斯皮尔曼相关系数**



```python
#两个Series，标签对齐
>>> s1 = pd.Series([1, 2, np.nan], index=[0, 1, 2])
>>> s2 = pd.Series([1, 2, 3], index=[2, 1, 0])
>>> s1.corr(s2)
np.float64(-0.9999999999999999)


#两个Series，存在标签未对齐的情况，返回nan
>>> s1 = pd.Series([1, 2, np.nan], index=[0, 1, 2])
>>> s2 = pd.Series([1, 2, 3], index=[2, 1, 5])
>>> s1.corr(s2)
np.float64(nan)


#method是一个可调用的对象/函数
>>> def histogram_intersection(a, b):
...     v = np.minimum(a, b).sum().round(decimals=1)
...     return v
>>> s1 = pd.Series([.2, .0, .6, .2])
>>> s2 = pd.Series([.3, .6, .0, .1])
>>> s1.corr(s2, method=histogram_intersection)
0.3
```





### DataFrame.corr

**==DataFrame.corr(*method='pearson', min_periods=1, numeric_only=False*)==**

​	**计算列的成对相关性，包括NA/null**



| 参数： |
| ------ |

**①method：{'pearson', 'kendall', 'spearman'} 或 callable**

- **pearson：皮尔逊系数，标准相关系数**
- **kendall: 肯德尔系数**
- **spearman：斯皮尔曼等级相关**
- **callable：输入是两个一维ndarray的可调用对象（函数）**

**②min_periods：int，可选**

​	**每列的最小观测数，只适用于皮尔逊和斯皮尔曼相关系数**

**③numeric_only：bool，默认False**

​	**是否只对数值型数据操作，数值型数据包括浮点数，整型和布尔型数据**



| 返回值： |
| -------- |

**:arrow_right:相关系数矩阵**



```python
df = pd.DataFrame([(1, 3, 1), (2, 3, 6), (5, 3, 4), (4, 4, 6)],
                  columns=['dogs', 'cats', 'fish'])
print("==================原DataFrame========================")
print(df)
print("==================生成相关系数矩阵,默认皮尔逊相关系数========================")
print(df.corr())
print("==================肯德尔相关系数矩阵========================")
print(df.corr(method='kendall'))
print("==================生成相关系数矩阵，设置最小观测量为2========================")
print(df.corr(min_periods=2))
print("==================生成相关系数矩阵，method参数传的是callable(可调用对象/函数)========================")
def histogram_intersection(a, b):
    v = np.minimum(a, b).sum().round(decimals=1)
    return v
print(df.corr(method=histogram_intersection))


#输出结果如下
==================原DataFrame========================
   dogs  cats  fish
0     1     3     1
1     2     3     6
2     5     3     4
3     4     4     6
==================生成相关系数矩阵,默认皮尔逊相关系数========================
          dogs      cats      fish
dogs  1.000000  0.365148  0.463600
cats  0.365148  1.000000  0.493742
fish  0.463600  0.493742  1.000000
==================肯德尔相关系数矩阵========================
          dogs      cats      fish
dogs  1.000000  0.235702  0.182574
cats  0.235702  1.000000  0.516398
fish  0.182574  0.516398  1.000000
==================生成相关系数矩阵，设置最小观测量为2========================
          dogs      cats      fish
dogs  1.000000  0.365148  0.463600
cats  0.365148  1.000000  0.493742
fish  0.463600  0.493742  1.000000
==================生成相关系数矩阵，method参数传的是callable(可调用对象/函数)========================
      dogs  cats  fish
dogs   1.0  10.0  11.0
cats  10.0   1.0  11.0
fish  11.0  11.0   1.0
```





### DataFrame.corrwith

**==DataFrame.corrwith(*other, axis=0, drop=False, method='pearson', numeric_only=False*)==**

​	**计算DataFrame的行或列与Series/DataFrame的行或列之间的成对相关性，计算前标签对齐**



| 参数： |
| ------ |

**①other：DataFrame，Series**

​	**指定与哪个对象计算相关性**

**②axis：{0 或 'index'，1 或 'columns'}，默认0**

​	**要沿哪个轴计算相关性**

**③drop: bool，默认False**

​	**从结果中删除缺失的索引**

**④method：{'pearson', 'kendall', 'spearman'} 或 callable**

- **pearson：皮尔逊系数，标准相关系数**
- **kendall: 肯德尔系数**
- **spearman：斯皮尔曼等级相关**
- **callable：输入是两个一维ndarray的可调用对象（函数）**

**⑤numeric_only：bool，默认False**

​	**是否只对数值型数据操作，数值型数据包括浮点数，整型和布尔型数据**



| 返回值： |
| -------- |

**:arrow_right:返回Series**



```python
index = ["a", "b", "c", "d", "e"]
columns = ["one", "two", "three", "four"]
df1 = pd.DataFrame(np.arange(20).reshape(5, 4), index=index, columns=columns)
df2 = pd.DataFrame(np.arange(16).reshape(4, 4), index=index[:4], columns=columns)
print("==================原DataFrame========================")
print(df1)
print(df2)
print("==================与DataFrame做运算，沿着轴0，计算两个DataFrame列的相关性========================")
print(df1.corrwith(df2))
print("==================与DataFrame做运算，沿着轴1，计算两个DataFrame行的相关性========================")
print(df1.corrwith(df2, axis=1))
ser1 = pd.Series([6, 3, 12, 5, 6], index=["a", "b", "c", "d", "e"])
ser2 = pd.Series([3, 4, 24, 14], index=["one", "two", "three", "four"])
print("==================与Series做运算，沿着轴0========================")
print(df1.corrwith(ser1))
print("==================与Series做运算，沿着轴1========================")
print(df1.corrwith(ser2, axis=1))


#输出结果如下
==================原DataFrame========================
   one  two  three  four
a    0    1      2     3
b    4    5      6     7
c    8    9     10    11
d   12   13     14    15
e   16   17     18    19
   one  two  three  four
a    0    1      2     3
b    4    5      6     7
c    8    9     10    11
d   12   13     14    15
==================与DataFrame做运算，沿着轴0，计算两个DataFrame列的相关性========================
one      1.0
two      1.0
three    1.0
four     1.0
dtype: float64
==================与DataFrame做运算，沿着轴1，计算两个DataFrame行的相关性========================
a    1.0
b    1.0
c    1.0
d    1.0
e    NaN						#这里NaN的原因是标签未对齐
dtype: float64
==================与Series做运算，沿着轴0========================
one      0.094072
two      0.094072
three    0.094072
four     0.094072
dtype: float64
==================与Series做运算，沿着轴1========================
a    0.695026
b    0.695026
c    0.695026
d    0.695026
e    0.695026
dtype: float64
```





### Series.cov

**==Series.cov(*other, min_periods=None, ddof=1*)==**

​	**计算两个序列的协方差，不包括缺失值，两个Series的长度不需要相同**



| 参数： |
| ------ |

**①other：Series**

​	**要和哪一个Series计算协方差，计算前需进行标签对齐，如果存在标签未对齐的情况，则返回`nan`**

**②min_periods：int，可选**

​	**最小观测数**

**③ddof: int, 默认为1**

​	**自由度**

- **ddof=0：总体协方差**
- **ddof=1：样本协方差（无偏估计）**

​	*使用以下计算方式*
$$
\mathrm{Cov}(X, Y) = \frac{1}{n-ddof} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})
$$


| 返回值： |
| -------- |

**:arrow_right:返回float：两个Series的协方差（无偏估计量）**



```python
>>> s1 = pd.Series([0.90010907, 0.13484424, 0.62036035])
>>> s2 = pd.Series([0.12528585, 0.26962463, 0.51111198])
>>> s1.cov(s2)
-0.01685762652715874
```





### DataFrame.cov

**==DataFrame.cov(*min_periods=None, ddof=1, numeric_only=False*)==**

​	**计算列的成对协方差，不包括NA/null值，生成协方差矩阵**
$$
\Sigma = \begin{bmatrix}
\text{Var}(X_1) & \text{Cov}(X_1, X_2) & \cdots & \text{Cov}(X_1, X_n) \\
\text{Cov}(X_2, X_1) & \text{Var}(X_2) & \cdots & \text{Cov}(X_2, X_n) \\
\vdots & \vdots & \ddots & \vdots \\
\text{Cov}(X_n, X_1) & \text{Cov}(X_n, X_2) & \cdots & \text{Var}(X_n)
\end{bmatrix}
$$


| 参数： |
| ------ |

**①min_periods：int， 可选**

​	**最小观测值。**

​	**计算前要进行标签对齐，每一列相当于一个样本空间，如果某个样本为NaN，属于无效数据，反之属于有效数据**

- **若有效数据量 $\ge$ `min_periods` ——> 正常计算**
- **若有效数据量 $\lt$ `min_periods` ——> 返回NaN**

**②ddof: int, 默认为1**

​	**自由度**

- **ddof=0：总体协方差**
- **ddof=1：样本协方差（无偏估计）**

​	*使用以下计算方式*
$$
\mathrm{Cov}(X, Y) = \frac{1}{n-ddof} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})
$$
**③numeric_only: bool，默认False**

​	**是否只处理数值型的数据，数值型数据包括浮点数，整数或布尔值**



| 返回值 |
| ------ |

**:arrow_right:返回协方差矩阵**



*一个简单例子*

```python
df = pd.DataFrame([(1, 2), (0, 3), (2, 0), (1, 1)],
                  columns=['dogs', 'cats'])
print("==================原DataFrame========================")
print(df)
print("==================DataFrame的协方差矩阵========================")
print(df.cov())


#输出结果如下
==================原DataFrame========================
   dogs  cats
0     1     2
1     0     3
2     2     0
3     1     1
==================DataFrame的协方差矩阵========================
          dogs      cats
dogs  0.666667 -1.000000
cats -1.000000  1.666667

```



**有一点需要说明，对于具有缺失值的DataFrame，返回的协方差矩阵不一定能保持其半正定性**

```python
np.random.seed(42)
df = pd.DataFrame(np.random.randn(20, 3),
                  columns=['a', 'b', 'c'])
print("==================原DataFrame========================")
print(df)
df.loc[df.index[:5], 'a'] = np.nan
df.loc[df.index[5:10], 'b'] = np.nan
print("==================修改后的DataFrame========================")
print(df)
print("==================修改后的DataFrame计算协方差矩阵，指定最小观测值为12========================")
print(df.cov(min_periods=12))


#输出结果如下
==================原DataFrame========================
           a         b         c
0   0.496714 -0.138264  0.647689
1   1.523030 -0.234153 -0.234137
2   1.579213  0.767435 -0.469474
3   0.542560 -0.463418 -0.465730
4   0.241962 -1.913280 -1.724918
5  -0.562288 -1.012831  0.314247
6  -0.908024 -1.412304  1.465649
7  -0.225776  0.067528 -1.424748
8  -0.544383  0.110923 -1.150994
9   0.375698 -0.600639 -0.291694
10 -0.601707  1.852278 -0.013497
11 -1.057711  0.822545 -1.220844
12  0.208864 -1.959670 -1.328186
13  0.196861  0.738467  0.171368
14 -0.115648 -0.301104 -1.478522
15 -0.719844 -0.460639  1.057122
16  0.343618 -1.763040  0.324084
17 -0.385082 -0.676922  0.611676
18  1.031000  0.931280 -0.839218
19 -0.309212  0.331263  0.975545
==================修改后的DataFrame========================
           a         b         c
0        NaN -0.138264  0.647689
1        NaN -0.234153 -0.234137
2        NaN  0.767435 -0.469474
3        NaN -0.463418 -0.465730
4        NaN -1.913280 -1.724918
5  -0.562288       NaN  0.314247
6  -0.908024       NaN  1.465649
7  -0.225776       NaN -1.424748
8  -0.544383       NaN -1.150994
9   0.375698       NaN -0.291694
10 -0.601707  1.852278 -0.013497
11 -1.057711  0.822545 -1.220844
12  0.208864 -1.959670 -1.328186
13  0.196861  0.738467  0.171368
14 -0.115648 -0.301104 -1.478522
15 -0.719844 -0.460639  1.057122
16  0.343618 -1.763040  0.324084
17 -0.385082 -0.676922  0.611676
18  1.031000  0.931280 -0.839218
19 -0.309212  0.331263  0.975545
==================修改后的DataFrame计算协方差矩阵，指定最小观测值为12========================
          a         b         c
a  0.316741       NaN -0.150812
b       NaN  1.248003  0.191417
c -0.150812  0.191417  0.895202
```

​		**这里解释一下最后这个结果，可以看到$\mathbf{Cov}(a, b) /$ $\mathbf{Cov}(b, a)$ 的结果为`NaN`，其调用函数为`df.cov(min_periods=12)`，设置了最小观测值为12，因为`a`和`b`两列的有效观测值为$10 \lt 12$，所以会返回NaN。**

**:heavy_exclamation_mark:<span style='color: red'>重要：关于`min_periods`参数</span>**

​		**DataFrame调用`cov()`时，其每一列当作一个样本空间，在计算前先进行标签对齐。可以看到修改后的df里面的`a`列有5行缺失值（也就是五个样本为NaN），属于5个无效观测值，也就是说：计算协方差时，$a_1, a_2, a_3, a_4, a_5$ 和 $b_1, b_2, b_3, b_4, b_5$不能计算（$a_i, b_i$表示第`i`个样本）；同理，对于`b`中的第五行到第十行的缺失值也是这样，也就是说一共有10个样本不能参与计算，现在总共有20个样本，则剩下的10个样本可以参与计算，是有效观测值。现在，调用`cov()`时传递了`min_periods = 12`，然而，DataFrame的样本空间的有效观测值达不到12个，所以会返回NaN**



### Series/DataFrame.pct_change

**==DataFrame.pct_change(*periods=1, freq=None, \*\*kwargs*)==**

​	**计算当前元素和先前元素之间的分数变化，默认计算相对于前一行的分数变化，此函数返回的是一个float，将结果乘100之后可以得到百分比变化**



| 参数： |
| ------ |

**①periods：int，默认1**

​	**观测值，相对于前periods个元素计算分数变化**

**②freq：DateOffset，timedelta或者str，可选**

​	**从时间序列API中增加使用量（例如ME或BDay()）**

**③\*\*kwargs**

​	**其他的关键字参数，可传递给DataFrame.shift或Series.shift方法的参数**



| 返回值： |
| -------- |

**:arrow_right:返回与调用对象相同类型的Series或DataFrame**



```python
#Series操作
------------------------------------------------------------------------------------
s = pd.Series([90, 91, 85])
print("============原Series==================")
print(s)
print("============Series的变化幅度,默认观测值为1==================")
print(s.pct_change())
print("============Series的百分比变化==================")
print(s.pct_change().apply(lambda x: f"{round(x * 100, 2)} %" if np.isnan(x) == False else "nan"))
print("============Series的分数变化,指定观测值为2==================")
print(s.pct_change(periods=2))


#输出结果如下
============原Series==================
0    90
1    91
2    85
dtype: int64
============Series的变化幅度,默认观测值为1==================
0         NaN
1    0.011111
2   -0.065934
dtype: float64
============Series的百分比变化==================
0        nan
1     1.11 %			#(91 - 90)/90 = 0.11
2    -6.59 %			#(85 - 91)/91 = -0.0659
dtype: object
============Series的分数变化,指定观测值为2==================
0         NaN
1         NaN
2   -0.055556
dtype: float64



#DataFrame操作
------------------------------------------------------------------------------------
#计算 1980 年 1 月 1 日至 1980 年 3 月 1 日法国法郎、德国马克和意大利里拉的百分比变化
df = pd.DataFrame({
    'FR': [4.0405, 4.0963, 4.3149],                 #法国
    'GR': [1.7246, 1.7482, 1.8519],                 #德国
    'IT': [804.74, 810.01, 860.13]},                #意大利
    index=['1980-01-01', '1980-02-01', '1980-03-01'])
print("============原DataFrame===============")
print(df)
print("============百分比变化===============")
print(df.pct_change())

#输出结果如下
============原DataFrame===============
                FR      GR      IT
1980-01-01  4.0405  1.7246  804.74
1980-02-01  4.0963  1.7482  810.01
1980-03-01  4.3149  1.8519  860.13
============百分比变化===============
                  FR        GR        IT
1980-01-01       NaN       NaN       NaN
1980-02-01  0.013810  0.013684  0.006549
1980-03-01  0.053365  0.059318  0.061876


# GOOG 和 APPL 股票交易量变化百分比。显示计算列之间的百分比变化。
df = pd.DataFrame({
    '2016': [1769950, 30586265],
    '2015': [1500923, 40912316],
    '2014': [1371819, 41403351]},
    index=['GOOG', 'APPL'])
print("=================原DataFrame==================")
print(df)
print("=================计算列之间的百分比==================")
print(df.pct_change(axis="columns", periods=-1))	#因为年份是倒序排列的，所以periods = -1,基于下一个观测值


#输出结果如下
=================原DataFrame==================
          2016      2015      2014
GOOG   1769950   1500923   1371819
APPL  30586265  40912316  41403351
=================计算列之间的百分比==================
          2016      2015  2014				# (2016 - 2015) / 2015
GOOG  0.179241  0.094112   NaN				# (1769950 - 1500923) / 1500923 = 0.179241 第一个数据
APPL -0.252395 -0.011860   NaN
```



### Series.value_counts ###

**==Series.value_counts(*normalize=False, sort=True, ascending=False, bins=None, dropna=True*)==**

​	**返回频次统计的Series，不包含缺失值，默认降序排列**



| 参数： |
| ------ |

**①normalize：bool，默认False**

​	**如果为True，则返回的对象包含唯一值的相对频率，即每个值的频次除以总频次得出的值**

**②sort：bool,默认为True**

​	**是否根据频次排序，如果为False，则保留原顺序**

**③ascending：bool,默认为False**

​	**如果为True，则升序排序，否则降序，默认为False**

**④bins: int,可选**

​	**不是对值进行计数，而是将它们分组到半开放的箱中，这很方便`pd.cut`，仅适用于数字数据**

**⑤dropna：bool，默认为True**

​	**是否包括NaN的计数**



```python
index = pd.Index([3, 1, 2, 3, 4, np.nan])

#默认降序排列
>>> index.value_counts()
3.0    2
1.0    1
2.0    1
4.0    1
Name: count, dtype: int64

#升序排序
>>> index.value_counts(ascending=True)
1.0    1
2.0    1
4.0    1
3.0    2
Name: count, dtype: int64

#计算每个词的相对频率 = 每个词出现的次数/总频次
>>> s = pd.Series([3, 1, 2, 3, 4, np.nan])
>>> s.value_counts(normalize=True)
3.0    0.4
1.0    0.2
2.0    0.2
4.0    0.2
Name: proportion, dtype: float64


#返回3个区间的频次， bins这个参数对于从连续变量转换为分类变量很有用
>>> s.value_counts(bins=3)
(0.996, 2.0]    2
(2.0, 3.0]      2
(3.0, 4.0]      1
Name: count, dtype: int64


#不删除NaN，并且对其计数
>>> s.value_counts(dropna=False)
3.0    2
1.0    1
2.0    1
4.0    1
NaN    1
Name: count, dtype: int64
```



### DataFrame.value_counts

**==DataFrame.value_counts(*subset=None, normalize=False, sort=True, ascending=False, dropna=True*)==**

​	**返回Series，此Series包含DataFrame每个不同行的频次统计，默认降序排列**

​	**返回的Series将具有一个多级索引，每个输入列对应一个level，但单个标签对应一个索引**



| 参数： |
| ------ |

**①subset：标签或标签列表，可选**

​	**要使用哪些列计算频次统计，默认所有列**

**②nomalize: bool，默认False**

​	**返回频次的比例（频次/总频次）而不是频次**

**③sort：bool，默认True**

​	**是否根据频次排序，如果为False，则保留原DataFrame的顺序**

**④ascending：bool,默认为False**

​	**如果为True，则升序排序，否则降序，默认为False**

**⑤dropna：bool，默认为True**

​	**是否包括NaN的计数**



```python
df = pd.DataFrame({'num_legs': [2, 4, 4, 6],
                   'num_wings': [2, 0, 0, 0]},
                  index=['falcon', 'dog', 'cat', 'ant'])
print("=================原DataFrame==================")
print(df)
print("=================频次统计，返回Series，其索引为多级索引，默认降序==================")
print(df.value_counts())
print("=================返回Series 其中的值是每个元素频次的比例==================")
print(df.value_counts(normalize=True))
print("=================频次统计，指定升序排序==================")
print(df.value_counts(ascending=True))
print("=================只对 num_wings 这列的值做频次统计 ==================")
print(df.value_counts("num_wings"))
print("=================只对 num_legs 这列的值做频次统计 ==================")
print(df.value_counts("num_legs"))



#输出结果如下
=================原DataFrame==================
        num_legs  num_wings
falcon         2          2
dog            4          0
cat            4          0
ant            6          0
=================频次统计，返回Series，其索引为多级索引，默认降序==================
num_legs  num_wings
4         0            2
2         2            1
6         0            1
Name: count, dtype: int64
=================返回Series 其中的值是每个元素频次的比例==================
num_legs  num_wings
4         0            0.50
2         2            0.25
6         0            0.25
Name: proportion, dtype: float64
=================频次统计，指定升序排序==================
num_legs  num_wings
2         2            1
6         0            1
4         0            2
Name: count, dtype: int64
=================只对 num_wings 这列的值做频次统计 ==================
num_wings
0    3
2    1
Name: count, dtype: int64
=================只对 num_legs 这列的值做频次统计 ==================
num_legs
4    2
2    1
6    1
Name: count, dtype: int64
```







## # 函数应用

### Series.apply

**==Series.apply(*func*)==**

​	**对Series的每个值调用func，函数可以是NumPy的`ufunc`，也可以是Python的函数**



```python
s = pd.Series([20, 21, 12],
              index=['London', 'New York', 'Helsinki'])
print(s)
print("===========NumPy的ufunc，sqrt===============")
print(s.apply(np.sqrt))
print("===========Python的函数===============")
def foo(values):
    return values + 3
print(s.apply(foo))

#运行结果如下
London      20
New York    21
Helsinki    12
dtype: int64
===========NumPy的ufunc，sqrt===============
London      4.472136
New York    4.582576
Helsinki    3.464102
dtype: float64
===========Python的函数===============
London      23
New York    24
Helsinki    15
dtype: int64

```



### DataFrame.apply

**==DataFrame.apply(*func, axis=0, raw=False, result_type=None*)==**

​	**对DataFrame中的每个列执行func函数，也可以对每一行应用func，修改`axis = 1`即可**



| 参数： |
| ------ |

**①func：function**

​	**应用于每一行或每一列的函数，可以是匿名函数**

**②axis：{0 或 'index'， 1 或 'columns'}， 默认为0**

​	**表示沿着哪个轴应用函数**

**③raw：bool ，默认False**

​	**确定行或列是否作为Series或ndarray对象传递**

- **`False`：将每行或每列作为一个Series传递给函数**
- **`True`：传递给函数的参数将改为接受ndarray对象，如果你只是应用NumPy的缩减函数，会有很好的性能**

**④result_type：{'expand', 'reduce', 'broadcast', None}，默认为None**

​	**仅在`axis=1`的时候此参数有效，设置结果的数据类型**



| 返回值： |
| -------- |

**:arrow_right:Series或DataFrame**

​	**沿DataFrame的给定轴应用函数的结果**



```python
df = pd.DataFrame(np.arange(10).reshape(5, 2), columns=['A', 'B'])
print(df)
print("=============每列的数据执行sqrt================")
print(df.apply(np.sqrt))
print("=============求每一列的和================")
print(df.apply(np.sum, axis=0))
print("=============求每一行的和================")
print(df.apply(np.sum, axis=1))
print("=============使用匿名函数，将每列的数据加1================")
print(df.apply(lambda x: x + 1))
print("=============使用匿名函数，用[1, 2, 3]沿着轴0填充================")
print(df.apply(lambda x: [1, 2, 3]))
print("=============使用匿名函数，用[1, 2, 3]沿着轴1填充================")
print(df.apply(lambda x: [1, 2, 3], axis=1))


#输出结果如下
   A  B
0  0  1
1  2  3
2  4  5
3  6  7
4  8  9
=============每列的数据执行sqrt================
          A         B
0  0.000000  1.000000
1  1.414214  1.732051
2  2.000000  2.236068
3  2.449490  2.645751
4  2.828427  3.000000
=============求每一列的和================
A    20
B    25
dtype: int64
=============求每一行的和================
0     1
1     5
2     9
3    13
4    17
dtype: int64
=============使用匿名函数，将每列的数据加1================
   A   B
0  1   2
1  3   4
2  5   6
3  7   8
4  9  10
=============使用匿名函数，用[1, 2, 3]沿着轴0填充================
   A  B
0  1  1
1  2  2
2  3  3
=============使用匿名函数，用[1, 2, 3]沿着轴1填充================
0    [1, 2, 3]
1    [1, 2, 3]
2    [1, 2, 3]
3    [1, 2, 3]
4    [1, 2, 3]
dtype: object

```





### Series.map

**==Series.map(*arg, na_action=None*)==**

​	**对Series中的每个值应用arg，arg返回的值可能来自函数、dict或Series**



| 参数： |
| ------ |

**①arg：function，collections.abc.Mapping 的子类 或 Series**

​	**映射对应关系**

​	**当`arg`是字典时，Series的值会和字典的键对齐，并且使用字典的值替换原来的Series中的值；如果Series中没有相应的标签，则数据为NaN，但是有一种例外，就是字典的子类提供了`__missing__`方法，此时会使用默认值而不是`NaN`**

**②na_action：{None, 'ignore'}，默认为None**

​	**如果为`ignore`，则NaN值保留，不会作为参数传递给arg**



| 返回值： |
| -------- |

**:arrow_right:返回与调用的Series含有相同索引的Series**





```python
s = pd.Series(['cat', 'dog', np.nan, 'rabbit'])
print(s)
print("===========arg传一个函数=================")
print(s.map("I am a {}".format))
print("===========忽略缺失值=================")
print(s.map("I am a {}".format, na_action='ignore'))
print("===========arg传一个字典=================")
print(s.map({'dog': 'cute', 'rabbit': 'dog'}))


#输出结果如下
0       cat
1       dog
2       NaN
3    rabbit
dtype: object
===========arg传一个函数=================
0       I am a cat
1       I am a dog
2       I am a nan
3    I am a rabbit
dtype: object
===========忽略缺失值=================
0       I am a cat
1       I am a dog
2              NaN
3    I am a rabbit
dtype: object
===========arg传一个字典=================
0     NaN
1    cute
2     NaN
3     dog
dtype: object


```





### DataFrame.map

**==DataFrame.map(*func, na_action=None, \*\*kwargs*)==**

​	**将DataFrame的每个元素应用于func，函数接受一个标量，返回一个标量到DataFrame的每个元素**



| 参数： |
| ------ |

**①func：callable**

​	**Python函数**

**②na_action：{None, 'ignore'}，默认`None`**

​	**如果为`ignore`，则NaN值保留，不会作为参数传递给func**

**③\*\*kwargs**

​	**func的其他附加关键字参数**



| 返回值 |
| ------ |

**:arrow_right:返回DataFrame**



```python
df = pd.DataFrame([[1, 2.12], [3.356, 4.567]])
print(df)
print("=============使用匿名函数======================")
print(df.map(lambda x: len(str(x))))
print("=============使用Python的函数，round还需传一个关键字参数，表示保留几位小数======================")
print(df.map(round, ndigits=2))
print("=============使用map 格式化字符串，保留两位小数======================")
print(df.map(lambda x: f"{x:.2f}"))
print("=============使用map 每个元素作平方操作======================")
print(df.map(lambda x: x ** 2))
print("=============平方的矢量化操作======================")
print(df ** 2)


#输出结果如下
       0      1
0  1.000  2.120
1  3.356  4.567
=============使用匿名函数======================
   0  1
0  3  4
1  5  5
=============使用Python的函数，round还需传一个关键字参数，表示保留几位小数======================
      0     1
0  1.00  2.12
1  3.36  4.57
=============使用map 格式化字符串，保留两位小数======================
      0     1
0  1.00  2.12
1  3.36  4.57
=============使用map 每个元素作平方操作======================
           0          1
0   1.000000   4.494400
1  11.262736  20.857489
=============平方的矢量化操作======================
           0          1
0   1.000000   4.494400
1  11.262736  20.857489


```







## # 缺失值处理

### Series/DataFrame/pandas.isna/isnull

**==pandas.isna/isnull(*obj*)==**

​	**检测`obj`中是否有缺失值，如果有，则返回`True`，否则返回`False`。**

​	**数字数组的缺失值为`NaN`，对象数组中的缺失值为`None`或`NaN`，datetimelike中的缺失值为`NaT`**



### Series/DataFrame/pandas.notna/notnull

**==pandas.notna/notnull(*obj*)==**

​	**相当于对 pandas.isna/isnull的结果全部取反**





### Series.dropna

**==Series.dropna(*axis=0, inplace=False, ignore_index=False*)==**

​	**返回一个移除缺失值的新Series**



| 参数： |
| ------ |

**①axis：{0 或 'index'}**

**②inplace：bool，默认False**

​	**如果为True，就地删除缺失值**

**③ignore_index: bool, 默认False**

​	**如果为True， 结果的索引为`0, 1, ..., n - 1`**



| 返回值： |
| -------- |

**:arrow_right:Series或None**

​	**如果`inplace = True`，则返回None，否则返回Series** 



```python
>>> ser = pd.Series([1., 2., np.nan])
>>> ser
0    1.0
1    2.0
2    NaN
dtype: float64

>>> ser.dropna()
0    1.0
1    2.0
dtype: float64


#空字符串不视为NA值，而None视为NA值
>>> ser = pd.Series([np.nan, 2, pd.NaT, '', None, 'I stay'])
>>> ser
0       NaN
1         2
2       NaT
3
4      None
5    I stay
dtype: object
>>> ser.dropna()
1         2
3
5    I stay
dtype: object
```





### DataFrame.dropna

**==DataFrame.dropna(*axis=0, how=\<no_default>, thresh=\<no_default>, subset=None, inplace=False, ignore_index=False*)==**

​	**移除缺失值**



| 参数： |
| ------ |

**①axis: {0 或 'index', 1 或 'columns'}, 默认0**

​	**指定沿着哪个轴删除缺失值**

**②how：{'any', 'all'}，默认'any'**

​	**`any`表示如果某列/行数据只要存在一个缺失值，则删除该行/列**

​	**`all`表示如果某行/列所有值都为NA，则删除该行/列**

**③thresh：int，可选**

​	**如果`thresh = n`，表示行/列中至少有n个非NA值才会删除该行/列，不能和how参数联用**

**④subset：列标签或标签序列，可选**

​	**指定对哪些列检查缺失值**

**⑤inplace：bool，默认False**

​	**如果为True，则就地删除NA值所在的行/列**

**⑥ignore_index: bool, 默认False**

​	**如果为True，则结果轴的标签为`0, 1, ..., n - 1`**



| 返回值： |
| -------- |

**:arrow_right:DataFrame或None**

​	**如果`inplace = True`，则返回None，否则返回DataFrame**



```python
df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]},
                  index=['a', 'b', 'c'])
print("===================原DataFrame=====================")
print(df)
print("===================沿着第一个轴 删除缺失值所在的行=====================")
print(df.dropna())
print("===================沿着第二个轴 删除缺失值所在的列=====================")
print(df.dropna(axis='columns'))
print("===================沿着第一个轴 只有行中所有值都是NA时才删除该行=====================")
print(df.dropna(how='all'))
print("===================沿着第一个轴 删除至少有2个非缺失值所在的行=====================")
print(df.dropna(thresh=2))
print("===================指定对 [\"toy", "name\"] 两列检查缺失值，如果存在缺失值则删除对应的行(axis=0决定)=====================")
print(df.dropna(subset=["toy", "name"]))
print("===================指定对 [\"a", "c\"] 两行检查缺失值，如果存在缺失值则删除对应的列(axis=1决定)=====================")
print(df.dropna(subset=['a', 'c'], axis='columns'))
print("===================沿着第一个轴 删除缺失值所在的行, 忽略其索引=====================")
print(df.dropna(ignore_index=True))
print("===================沿着第二个轴 删除缺失值所在的列, 忽略其索引=====================")
print(df.dropna(axis='columns', ignore_index=True))
print("===================原地删除缺失值，会返回None=====================")
print(df.dropna(inplace=True))
print("===================再来看原来的数据=====================")
print(df)




#输出结果如下

===================原DataFrame=====================
       name        toy       born
a    Alfred        NaN        NaT
b    Batman  Batmobile 1940-04-25
c  Catwoman   Bullwhip        NaT
===================沿着第一个轴 删除缺失值所在的行=====================
     name        toy       born
b  Batman  Batmobile 1940-04-25
===================沿着第二个轴 删除缺失值所在的列=====================
       name
a    Alfred
b    Batman
c  Catwoman
===================沿着第一个轴 只有行中所有值都是NA时才删除该行=====================
       name        toy       born
a    Alfred        NaN        NaT
b    Batman  Batmobile 1940-04-25
c  Catwoman   Bullwhip        NaT
===================沿着第一个轴 删除至少有2个非缺失值所在的行=====================
       name        toy       born
b    Batman  Batmobile 1940-04-25
c  Catwoman   Bullwhip        NaT
===================指定对 ["toy name"] 两列检查缺失值，如果存在缺失值则删除对应的行(axis=0决定)=====================
       name        toy       born
b    Batman  Batmobile 1940-04-25
c  Catwoman   Bullwhip        NaT
===================指定对 ["a c"] 两行检查缺失值，如果存在缺失值则删除对应的列(axis=1决定)=====================
       name
a    Alfred
b    Batman
c  Catwoman
===================沿着第一个轴 删除缺失值所在的行, 忽略其索引=====================
     name        toy       born
0  Batman  Batmobile 1940-04-25
===================沿着第二个轴 删除缺失值所在的列, 忽略其索引=====================
       name
0    Alfred
1    Batman
2  Catwoman
===================原地删除缺失值，会返回None=====================
None
===================再来看原来的数据=====================
     name        toy       born
b  Batman  Batmobile 1940-04-25
```





### Series/DataFrame.fillna

**==Series/DataFrame.fillna(*value=None, axis=None, inplace=False, limit=None*)==**

​	**使用value填充缺失值**



| 参数： |
| ------ |

**①value：标量，字典，Series或DataFrame**

​	**用于填充缺失值的value**

**②axis：{0 or 'index'} 对于 Series，{0 或 'index'，1 或'columns'}对于DataFrame**

​	**沿着哪个轴填充缺失值**

**③inplace：bool，默认False**

​	**如果为True，则就地填充缺失值**

**④limit：int 默认None**

​	**指定向前/向后 填充 的连续缺失值的 最大数量**



```python
df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, np.nan],
                   [np.nan, 3, np.nan, 4]],
                  columns=list("ABCD"),
                  index=list('pear'))
print("===================原DataFrame=====================")
print(df)
print("===================value = 标量,用0填充=====================")
print(df.fillna(0))
print("===================value = dict=====================")
values_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4.0}
print(df.fillna(value=values_dict))
print("===================value = dict, 限制填充一个值=====================")
print(df.fillna(value=values_dict, limit=1))
print("===================value = DataFrame，则必须标签对齐，会进行标签对齐填充对应的数据=====================")
fill_df = pd.DataFrame(np.ones((4, 4)), columns=list("ABCD"), index=list('epra'))
print(df.fillna(value=fill_df))
print("===================原地填充缺失值，会返回None=====================")
print(df.fillna(0, inplace=True))
print("===================再来看原来的数据=====================")
print(df)



===================原DataFrame=====================
     A    B   C    D
p  NaN  2.0 NaN  0.0
e  3.0  4.0 NaN  1.0
a  NaN  NaN NaN  NaN
r  NaN  3.0 NaN  4.0
===================value = 标量,用0填充=====================
     A    B    C    D
p  0.0  2.0  0.0  0.0
e  3.0  4.0  0.0  1.0
a  0.0  0.0  0.0  0.0
r  0.0  3.0  0.0  4.0
===================value = dict=====================
     A    B    C    D					#A列用1，B列用2，C列用3，D列用4
p  1.0  2.0  3.0  0.0
e  3.0  4.0  3.0  1.0
a  1.0  2.0  3.0  4.0
r  1.0  3.0  3.0  4.0
===================value = dict, 限制填充一个值=====================
     A    B    C    D
p  1.0  2.0  3.0  0.0
e  3.0  4.0  NaN  1.0
a  NaN  2.0  NaN  4.0
r  NaN  3.0  NaN  4.0
===================value = DataFrame，则必须标签对齐，会进行标签对齐填充对应的数据=====================
     A    B    C    D
p  1.0  2.0  1.0  0.0
e  3.0  4.0  1.0  1.0
a  1.0  1.0  1.0  1.0
r  1.0  3.0  1.0  4.0
===================原地填充缺失值，会返回None=====================
None
===================再来看原来的数据=====================
     A    B    C    D
p  0.0  2.0  0.0  0.0
e  3.0  4.0  0.0  1.0
a  0.0  0.0  0.0  0.0
r  0.0  3.0  0.0  4.0
```





### Series/DataFrame.ffill/bfill

**==Series/DataFrame.ffill/bfill(*axis=None, inplace=False, limit=None, limit_area=None*)==**

​	**向前或向后填充缺失值**



## # 去重，转换，替换

### Series.duplicated

**==Series.duplicated(*keep='first'*)==**

​	**返回一个Series[bool]， 重复值使用`True`标记。**



| 参数： |
| ------ |

**keep: {'first', 'last', False}, 默认 'first'**

- **如果为'first'，则把重复项的第一个标记为False，其他的标记为True**
- **如果为'last'，则把重复项中的最后一个标记为False，其他的标记为True**
- **如果为False，将所有的重复项标记为True**



**:arrow_right:返回Series[bool]**



```python
>>> animals = pd.Series(['llama', 'cow', 'llama', 'beetle', 'llama'])
>>> animals.duplicated()			#默认keep = first
0    False
1    False
2     True
3    False
4     True
dtype: bool


>>> animals.duplicated(keep='first')
0    False
1    False
2     True
3    False
4     True
dtype: bool


#把最后一个出现的重复项标记为False，也就是在drop_duplicates的时候保留最后一项，其他标记为True
>>> animals.duplicated(keep='last')
0     True
1    False
2     True
3    False
4    False
dtype: bool


#把所有重复值都标记为True
>>> animals.duplicated(keep=False)
0     True
1    False
2     True
3    False
4     True
dtype: bool
```





### DataFrame.duplicated

**==DataFrame.duplicated(*subset=None, keep='first'*)==**

​	**返回标记重复行的布尔值的Series，如果指定了subset，则仅查找某些列的重复项**



| 参数： |
| ------ |

**①subset：列标签 或 标签序列，可选**

​	**表示对哪些列进行重复项标记，默认对所有列**

**②keep：{'first', 'last', False}，默认'first'**

- **如果为'first'，则把重复项的第一个标记为False，其他的标记为True**
- **如果为'last'，则把重复项中的最后一个标记为False，其他的标记为True**
- **如果为False，将所有的重复项标记为True**



**:arrow_right:返回Series[bool]，其索引是原DataFrame的行索引，values是布尔值（对列重复项的观察）**





```python
df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]})
print("===================原DataFrame=====================")
print(df)
print("===================标记重复行，重复项的第一个标记为False，其他标记为True=====================")
print(df.duplicated())
print("===================标记重复行，重复项的最后一个标记为False，其他标记为True=====================")
print(df.duplicated(keep='last'))
print("===================标记重复行，所有重复项都标记为False=====================")
print(df.duplicated(keep=False))
print("===================标记重复行，仅对'rating'列检查重复值=====================")
print(df.duplicated(subset='rating'))
print("===================标记重复行，对['rating', 'brand']两列检查重复值=====================")
print(df.duplicated(subset=['brand', 'rating']))



#输出结果如下
===================原DataFrame=====================
     brand style  rating
0  Yum Yum   cup     4.0
1  Yum Yum   cup     4.0
2  Indomie   cup     3.5
3  Indomie  pack    15.0
4  Indomie  pack     5.0
===================标记重复行，重复项的第一个标记为False，其他标记为True=====================
0    False
1     True
2    False
3    False
4    False
dtype: bool
===================标记重复行，重复项的最后一个标记为False，其他标记为True=====================
0     True
1    False
2    False
3    False
4    False
dtype: bool
===================标记重复行，所有重复项都标记为False=====================
0     True
1     True
2    False
3    False
4    False
dtype: bool
===================标记重复行，仅对'rating'列检查重复值=====================
0    False
1     True
2    False
3    False
4    False
dtype: bool
===================标记重复行，对['rating', 'brand']两列检查重复值=====================
0    False
1     True
2    False
3    False
4    False
dtype: bool
```





### Series.drop_duplicates

**==Series.drop_duplicates(*keep='first', inplace=True, ignore_index=False*)==**

​	**返回移除重复值的Series**



| 参数： |
| ------ |

**①keep: {'first', 'last', False}，默认'first'**

​	**处理删除缺失数据的方法**

- **'first'：删除 除第一个出现的重复项**
- **'last'：删除 除最后一个出现的重复项**
- **False：删除所有重复项**

**②inplace：bool，默认False**

​	**如果为True，则就地删除重复项**

**③ignore_index：bool，默认False**

​	**如果为True，则输出结果的索引为`0, 1, ..., n-1`**



| 返回值： |
| -------- |

**:arrow_right:Series或None**

​	**如果`inplace = True`，则返回None，否则返回删除重复项的Series**



```python
>>> s = pd.Series(['llama', 'cow', 'llama', 'beetle', 'llama', 'hippo'],
...               name='animal')
>>> s
0     llama
1       cow
2     llama
3    beetle
4     llama
5     hippo
Name: animal, dtype: object


>>> s.drop_duplicates()
0     llama
1       cow
3    beetle
5     hippo
Name: animal, dtype: object


>>> s.drop_duplicates(keep='last')
1       cow
3    beetle
4     llama
5     hippo
Name: animal, dtype: object


>>> s.drop_duplicates(keep=False)
1       cow
3    beetle
5     hippo
Name: animal, dtype: object


s = pd.Series(['llama', 'cow', 'llama', 'beetle', 'llama', 'hippo'],
              name='animal')
print(s.drop_duplicates(inplace=True))
print(s)

#输出结果如下
None
0     llama
1       cow
3    beetle
5     hippo
Name: animal, dtype: object
```





### DataFrame.drop_duplicates

**==DataFrame.drop_duplicates(*subset=None, keep='first', inplace=False, ignore_index=False*)==**

​	**返回已删除重复行的DataFrame，可以指定对哪些列的重复项做观察**



| 参数： |
| ------ |

**①subset：列标签或标签序列，可选**

​	**指定对哪些列来识别重复项，默认情况下使用所有列**

**②keep: {'first', 'last', False}，默认 'first'**

​	**指定要保留哪些重复项**

- **'first'：保留重复项中第一次出现的元素，其他的删除**
- **'last'：保留重复项中最后一次出现的元素，其他的删除**
- **False：删除所有重复项**

**③inplace：bool，默认False**

​	**如果为True，则就地删除重复项，否则生成新的DataFrame**

**④ignore_index：bool，默认False**

​	**如果为True，则输出结果的轴标签为`0, 1, ..., n - 1`**



| 返回值： |
| -------- |

**:arrow_right:DataFrame 或 None**

​	**如果`inplace = True`，则返回None，否则返回新的DataFrame**



```python
df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
},
index=list('apple'))
print("===================原DataFrame=====================")
print(df)
print("===================对DataFrame的所有列进行观察，删除重复行=====================")
print(df.drop_duplicates())
print("===================对DataFrame的['brand', 'style'] 列进行观察，删除重复行=====================")
print(df.drop_duplicates(subset=['brand', 'style']))
print("===================对DataFrame的所有列进行观察，默认保留第一个重复项，相当于keep = first=====================")
print(df.drop_duplicates(keep='first'))
print("===================对DataFrame的所有列进行观察，keep = last,保留最后一个重复项=====================")
print(df.drop_duplicates(keep='last'))
print("===================对DataFrame的所有列进行观察，keep = False 不保留任何一个重复项=====================")
print(df.drop_duplicates(keep=False))
print("===================对DataFrame的所有列进行观察，忽略原先DataFrame的行索引，使用0 —— n-1=====================")
print(df.drop_duplicates(ignore_index=True))



#输出结果如下
===================原DataFrame=====================
     brand style  rating
a  Yum Yum   cup     4.0
p  Yum Yum   cup     4.0
p  Indomie   cup     3.5
l  Indomie  pack    15.0
e  Indomie  pack     5.0
===================对DataFrame的所有列进行观察，删除重复行，默认保留第一个重复项=====================
     brand style  rating
a  Yum Yum   cup     4.0
p  Indomie   cup     3.5
l  Indomie  pack    15.0
e  Indomie  pack     5.0
===================对DataFrame的['brand', 'style'] 列进行观察，删除重复行=====================
     brand style  rating
a  Yum Yum   cup     4.0
p  Indomie   cup     3.5
l  Indomie  pack    15.0
===================对DataFrame的所有列进行观察，默认保留第一个重复项，相当于keep = first=====================
     brand style  rating
a  Yum Yum   cup     4.0
p  Indomie   cup     3.5
l  Indomie  pack    15.0
e  Indomie  pack     5.0
===================对DataFrame的所有列进行观察，keep = last,保留最后一个重复项=====================
     brand style  rating
p  Yum Yum   cup     4.0
p  Indomie   cup     3.5
l  Indomie  pack    15.0
e  Indomie  pack     5.0
===================对DataFrame的所有列进行观察，keep = False 不保留任何一个重复项=====================
     brand style  rating
p  Indomie   cup     3.5
l  Indomie  pack    15.0
e  Indomie  pack     5.0
===================对DataFrame的所有列进行观察，忽略原先DataFrame的行索引，使用0 —— n-1=====================
     brand style  rating
0  Yum Yum   cup     4.0
1  Indomie   cup     3.5
2  Indomie  pack    15.0
3  Indomie  pack     5.0
```





### Series/DataFrame.replace

**==Series/DataFrame.replace(*to_replace=None, value=\<no_default>, inplace=False, regex=False*)==**

​	**使用给定的value去替换to_replace的值**



| 参数： |
| ------ |

**①to_replace：str、regex、list、dict、Series、int、float 或 None**

​	**怎么找到将被替换的值**

- **数字，str或regex**
  - **数字：等于to_replace的数字被替换成value**
  - **str：与to_replace完全匹配的字符串被替换成value**
  - **regex：与to_replace完全匹配的正则表达式被替换成value**
- **str的列表、regex的列表或数字的列表**
  - **首先，如果to_replace和value都是列表，则它们必须等长**
  - **其次，如果`regex = True`，则在两个列表中（to_replace和value）的所有字符串都会被解释为regex，否则将直接匹配。这对于value来说影响不大，因为可用的替换的regex只有几个**
- **dict**
  - **字典可以为不同的现有值指定不同的替换值，字典的键是现有值，值是替换值，此时方法的value参数不应指定。**
  - **对于DataFrame来说，dict可以指定在不同的列中替换不同的值，这个情况下，字典的键是列名，值是现有值，此时value参数必须传递。**
  - **对于嵌套字典的DataFrame，例如`{'a': {'b': np.nan}}`，其中a是列名，b是现有值，np.nan是替换值，此时value参数不应指定。你也可以嵌套正则表达式，但是列名不能是正则表达式**
- **None**
  - **这意味着regex参数必须是字符串、已编译的正则表达式或者包含此类元素的列表、字典、ndarray或Series。如果value参数也是None，则此参数必须是嵌套的字典或Series**

**②value：标量，dict，列表，str，regex，默认None**

​	**用于替换 任何与to_replace匹配的值**

**③inplace: bool,默认False**

​	**如果为True，则就地替换对应的值**

**④regex: bool 或 与to_replace的相同类型，默认False**

​	**是否将to_replace 和value解释为正则表达式**



| 返回值： |
| -------- |

**:arrow_right:返回替换后的Series或DataFrame**





**:one:`to_replace`和`value`都是标量**

```python
s = pd.Series([1, 2, 3, 4, 5])
>>> print(s.replace(2, 6))

0    1
1    6
2    3
3    4
4    5
dtype: int64


----------------------------------------------------------------------------------------------------
df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 0, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})
>>> print(df.replace(0, 12))
    A   B  C
0  12   5  a
1   1   6  b
2   2  12  c
3   3   8  d
4   4   9  e
```





**:two:`to_replace`是类列表**

```python
s = pd.Series([1, 2, 3, 4, 5])
>>> print(s.replace([1, 2], 6))			#使用6替换[1, 2]
0    6
1    6
2    3
3    4
4    5
dtype: int64


>>> print(s.replace([1, 2], [6, 7]))		#使用[6, 7]替换[1, 2]
0    6
1    7
2    3
3    4
4    5
dtype: int64


----------------------------------------------------------------------------------------------------

df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 0, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']},
                  index=list("apple"))
>>> print(df.replace([5, 6, 1, 3], 2))		#使用2替换DataFrame中的[5, 6, 1, 3]
   A  B  C
a  0  2  a
p  2  2  b
p  2  0  c
l  2  8  d
e  4  9  e


>>> print(df.replace([5, 6, 1, 3], [1, 2, 3, 4]))		#使用value列表替换to_replace列表
   A  B  C
a  0  1  a
p  3  2  b
p  2  0  c
l  4  8  d
e  4  9  e

```





**:three:to_place是字典**

```python
s = pd.Series([1, 2, 3, 4, 5], index=list('abcde'))
print("==================原Series=======================")
print(s)
print("==================使用dict进行替换，键是现有值，值是替换值=======================")
print(s.replace({1: np.nan, 5: 6}))


#输出结果如下
==================原Series=======================
a    1
b    2
c    3
d    4
e    5
dtype: int64
==================使用dict进行替换，键是现有值，值是替换值=======================
a    NaN
b    2.0
c    3.0
d    4.0
e    6.0
dtype: float64



----------------------------------------------------------------------------------------------------
df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 0, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']},
                  index=list("apple"))
print("==================原DataFrame=======================")
print(df)
print("==================使用dict替换DataFrame里面具体的值，则dict{现有值: 替换值}=======================")
print(df.replace({0: np.nan, 'a': 'x', 9: 100}))
print("==================使用dict，对某些列的某些值进行替换，dict为{col：现有值}，此时必须指定value=======================")
print(df.replace({'A': [2, 3], 'B': 5, 'C': 'd'}, value=100))
print("==================使用嵌套的dict替换DataFrame里面具体的值，则dict{col: {现有值: 替换值}}=======================")
print(df.replace({'A': {0:np.nan}, 'B': {0:100}}))



#输出结果如下
==================原DataFrame=======================
   A  B  C
a  0  5  a
p  1  6  b
p  2  0  c
l  3  8  d
e  4  9  e
==================使用dict替换DataFrame里面具体的值，则dict{现有值: 替换值}=======================
     A      B  C
a  NaN    5.0  x
p  1.0    6.0  b
p  2.0    NaN  c
l  3.0    8.0  d
e  4.0  100.0  e
==================使用dict，对某些列的某些值进行替换，dict为{col：现有值}，此时必须指定value=======================
     A    B    C
a    0  100    a
p    1    6    b
p  100    0    c
l  100    8  100
e    4    9    e
==================使用嵌套的dict替换DataFrame里面具体的值，则dict{col: {现有值: 替换值}}=======================
     A    B  C
a  NaN    5  a
p  1.0    6  b
p  2.0  100  c
l  3.0    8  d
e  4.0    9  e
```



**:four:to_place是正则表达式**

```python
df = pd.DataFrame({'A': ['bat', 'foo', 'bait'],
                   'B': ['abc', 'bar', 'xyz']})
print("===============原DataFrame===================")
print(df)
print("===============regex = True，匹配以b开头，后面是任意数量的字母或数字的字符串，将其替换为new===================")
print(df.replace(r"^b\w*", "new", regex=True))
print("===============regex = True，在A列中 匹配以b开头，后面是任意数量的字母或数字的字符串，将其替换为new===================")
print(df.replace({'A': r"^b\w*"}, {'A': "new"}, regex=True))
print("===============regex = str，value通过关键字参数传递，将匹配 ^fo+ 的字符串替换为func===================")
print(df.replace(regex=r"^fo+", value="func"))
print("===============regex = list，value通过关键字参数传递，将匹配 ^x\\w+和foo 的字符串替换为new===================")
print(df.replace(regex=[r"^x\w*", 'foo'], value="new"))
print("===============regex = dict，字典的键是现有值，值是替换值，此参数下，键可以是正则表达式===================")
print(df.replace(regex={r"^x\w*": "new", "abc": "cap"}))




#输出结果如下
===============原DataFrame===================
      A    B
0   bat  abc
1   foo  bar
2  bait  xyz
===============regex = True，匹配以b开头，后面是任意数量的字母或数字的字符串，将其替换为new===================
     A    B
0  new  abc
1  foo  new
2  new  xyz
===============regex = True，在A列中 匹配以b开头，后面是任意数量的字母或数字的字符串，将其替换为new===================
     A    B
0  new  abc
1  foo  bar
2  new  xyz
===============regex = str，value通过关键字参数传递，将匹配 ^fo+ 的字符串替换为func===================
      A    B
0   bat  abc
1  func  bar
2  bait  xyz
===============regex = list，value通过关键字参数传递，将匹配 ^x\w+和foo 的字符串替换为new===================
      A    B
0   bat  abc
1   new  bar
2  bait  new
===============regex = dict，字典的键是现有值，值是替换值，此参数下，键可以是正则表达式===================
      A    B		  #regex={r"^x\w*": "new", "abc": "cap"}
0   bat  cap
1   foo  bar
2  bait  new
```







## # 离散化和分箱

### pandas.cut

**==pandas.cut(*x, bins, right=True, labels=None, retbins=False, precision=3, include_lowset=False, duplicates='raise', ordered=True*)==**

​	**将值分成离散区间，可以将数据分箱到相同数量的箱体中，或分箱到预先指定的数组中。**

​	**任何NA值在结果中都将为NA，超出范围的值在生成的Series或Categorical对象中也为NA**



| 参数： |
| ------ |

**①x: array_like**

​	**需要分箱的输入数组，必须是一维的**

**②bins：int，标量的序列 或 IntervalIndex**

​	**分箱的标准**

- **int：如果`bins = n`，则表示将x等分为n个区间。x的取值范围向两边扩展0.1%，以包含最大值和最小值**
- **标量序列：其中的标量为分箱的边界，区间是左开右闭的，x的取值范围未进行扩展**
- **IntervalIndex：定义要使用确切的区间进行分箱，此时分箱的区间不能重叠**

**③right：bool，默认True**

​	**指定箱是否包含最右边缘，如果为True，则箱是左开右闭区间，否则为左闭右开区间。**

​	**如果`bins`参数是IntervalIndex，此参数会被忽略**

**④labels：数组或False，默认None**

​	**指定返回bin的标签，其长度必须与结果bin的长度相同。如果为False，则仅返回bin的整数指示符。**

​	**如果`bins`参数是IntervalIndex，此参数会被忽略。**

​	**当`ordered = False`时，此参数必须提供**

**⑤retbins：bool，默认False**

​	**是否返回bins，如果bins为标量时可以清楚地看到区间**

**⑥precision：int，默认3**

​	**指定bins标签的精度**

**⑦include_lowest：bool，默认False**

​	**指定分箱的第一个区间是否应该包含左区间**

**⑧duplicates：{默认'raise', 'drop'}，可选**

​	**如果箱的边缘不唯一，则引发[ValueError][]或删除重复值**

**⑨ordered：bool，默认True**

​	**是否对分箱的标签进行排序**



| 返回值： |
| -------- |

**:arrow_right:out：Categorical，Series 或 ndarray**

​	**返回一个类似数组的对象，表示x的每个值对应的bin，类型取决于label值**

**:arrow_right:bins：numpy.ndarray 或 IntervalIndex**

​	**计算或指定的bins，仅在`retbins = True`的时候返回。**





```python
# bin = 标量
----------------------------------------------------------------------------------------------------
# 被分箱的x为NumPy的ndarray
arr = np.array([1, 7, 5, 4, 6, 3])
print(f"原数组： {arr}")
print("================分箱成三个区间，默认返回的分类对象有序====================")
print(pd.cut(arr, 3))
print("================分箱成三个区间,返回分箱的边界值====================")
print(pd.cut(arr, 3, retbins=True))
print("================分箱成三个区间，指定每个分箱的标签====================")
print(pd.cut(arr, 3, labels=['small', 'medium', 'big']))
print("================分箱成三个区间，指定分类对象无序，这是labels可以是重复标签====================")
print(pd.cut(arr, 3, labels=['small', 'medium', 'small'], ordered=False))
print("================分箱成三个区间，label = False表示原数组对应的分箱的编号====================")
print(pd.cut(arr, 3, labels=False))



#输出结果如下
原数组： [1 7 5 4 6 3]
================分箱成三个区间，默认返回的分类对象有序====================
[(0.994, 3.0], (5.0, 7.0], (3.0, 5.0], (3.0, 5.0], (5.0, 7.0], (0.994, 3.0]]
Categories (3, interval[float64, right]): [(0.994, 3.0] < (3.0, 5.0] < (5.0, 7.0]]
================分箱成三个区间,返回分箱的边界值====================
([(0.994, 3.0], (5.0, 7.0], (3.0, 5.0], (3.0, 5.0], (5.0, 7.0], (0.994, 3.0]]
Categories (3, interval[float64, right]): [(0.994, 3.0] < (3.0, 5.0] < (5.0, 7.0]], array([0.994, 3.   , 5.   , 7.   ]))
================分箱成三个区间，指定每个分箱的标签====================
['small', 'big', 'medium', 'medium', 'big', 'small']
Categories (3, object): ['small' < 'medium' < 'big']
================分箱成三个区间，指定分类对象无序，这是labels可以是重复标签====================
['small', 'small', 'medium', 'medium', 'small', 'small']
Categories (2, object): ['medium', 'small']
================分箱成三个区间，label = False表示原数组对应的分箱的编号====================
[0 2 1 1 2 0]

                                                           
                                                           
#被分箱的x为Series                                                           
s = pd.Series(np.array([2, 4, 6, 8, 10]),
              index=['a', 'b', 'c', 'd', 'e'])
print("==============原Series====================")
print(s)
print("==============将Series的值等分成三个区间（箱）====================")
print(pd.cut(s, 3))
print("==============将Series的值等分成三个区间（箱），right = False 表示区间左闭右开====================")
print(pd.cut(s, 3, right=False))
                                                           


# bins = 一维数组                                                           
----------------------------------------------------------------------------------------------------         ages = np.array([10, 15, 13, 12, 23, 25, 28, 59, 60])
>>> print(pd.cut(ages, bins=[0, 12, 18, 50, 90]))                                                  
[(0, 12], (12, 18], (12, 18], (0, 12], (18, 50], (18, 50], (18, 50], (50, 90], (50, 90]]
Categories (4, interval[int64, right]): [(0, 12] < (12, 18] < (18, 50] < (50, 90]]                                                           
     
                                                                          
#	bins = IntervalIndex对象                                                       
----------------------------------------------------------------------------------------------------         pd.cut(ages, bins=pd.IntervalIndex.from_breaks([0, 40, 70]))                                                 
[(0, 40], (0, 40], (0, 40], (0, 40], (0, 40], (0, 40], (0, 40], (40, 70], (40, 70]]
Categories (2, interval[int64, right]): [(0, 40] < (40, 70]]
```



**一个不错的例子**

```python
df = pd.DataFrame({"value": np.random.randint(0, 100, 15)})
labels = ["{0} - {1}".format(i, i + 9) for i in range(0, 100, 10)]
df["group"] = pd.cut(df.value, range(0, 105, 10), right=False, labels=labels)
print(df)
print("==================DataFrame每列的数据类型===============")
print(df.dtypes)
print("==================DataFrame数据类型为category的列===============")
print(df['group'])


    value    group
0      37  30 - 39
1      33  30 - 39
2      91  90 - 99
3      92  90 - 99
4       8    0 - 9
5      36  30 - 39
6      21  20 - 29
7       9    0 - 9
8      64  60 - 69
9      50  50 - 59
10      2    0 - 9
11     45  40 - 49
12     91  90 - 99
13     60  60 - 69
14     72  70 - 79
==================DataFrame每列的数据类型===============
value       int32
group    category
dtype: object
==================DataFrame数据类型为category的列===============
0     30 - 39
1     30 - 39
2     90 - 99
3     90 - 99
4       0 - 9
5     30 - 39
6     20 - 29
7       0 - 9
8     60 - 69
9     50 - 59
10      0 - 9
11    40 - 49
12    90 - 99
13    60 - 69
14    70 - 79
Name: group, dtype: category
Categories (10, object): ['0 - 9' < '10 - 19' < '20 - 29' < '30 - 39' ... '60 - 69' < '70 - 79' < '80 - 89' < '90 - 99']

#提示
>>> list(range(0, 105, 10))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```





### pandas.qcut

**==pandas.qcut(*x, q, labels=None, retbins=False, precision=3, duplicates='raise'*)==**

​	**基于分位数的离散化函数，根据秩或样本的分位数将变量离散化为大小相等的桶。**

​	**如果某个值超出了分箱的范围，则会被标记为NA**



| 参数： |
| ------ |

**①x：一维ndarray 或Series**

**②q：int 或 float的列表**

​	**分位数的数量，例如四分位数`q = 4`，或者自定义的分位数列表`q = [0, 0.1, 0.4, 0.7, 1.0]`**

**③labels：数组 或 False，默认None**

​	**指定结果分箱bin的标签，标签数组的长度必须与bins等长，如果为False，其每个bin的标签为整数，如果为True，会引发error**

**④retbins：bool，可选**

​	**指定是否返回`(bins, labels)`**

**⑤precision: int，可选**

​	**指定bins标签的精度，默认3**

**⑥duplicates：{default 'raise', 'drop'}，可选**

​	**如果bin的边缘不唯一，则引发[ValueError][]或删除重复值**



| 返回值： |
| -------- |

**:arrow_right:out：Categorical 或 Series 或 整数数组（如果`labels = False`）**

​	**返回的数据类型取决于输入的类型**

**:arrow_right:bins：浮点数的ndarray**

​	**只有`rebins = True`的时候返回**





```python
>>> pd.qcut(range(5), 4)
[(-0.001, 1.0], (-0.001, 1.0], (1.0, 2.0], (2.0, 3.0], (3.0, 4.0]]
Categories (4, interval[float64, right]): [(-0.001, 1.0] < (1.0, 2.0] < (2.0, 3.0] < (3.0, 4.0]]

>>> pd.qcut(range(5), 3, labels=["good", "medium", "bad"])                                                   ['good', 'good', 'medium', 'bad', 'bad']
Categories (3, object): ['good' < 'medium' < 'bad'] 

>>> pd.qcut(range(5), 4, labels=False)                                                                       array([0, 0, 1, 2, 3], dtype=int64)           
```





## # 虚拟变量转换

### pandas.get_dummies

**==pandas.get_dummies(*data, prefix=None, prefix_sep='_', dummy_na=False, columns=None, sparse=False, drop_first=False, dtype=None*)==**

​	**将Categorical变量转换为虚拟变量/指示变量，每个变量都会转换为与值数量相同的0/1变量，输出中的每列都以值命名。如果输入是DataFrame，则原始变量的名称将添加到值前面。**

​	**注意，默认情况下，这个方法只会转换dtype为`object、string、category`的变量，其他的不作操作**



| 参数： |
| ------ |

**①data：array_like，Series 或DataFrame**

​	**输入数据**

**②prefix：str, str的列表或str的字典，默认None**

​	**用于附加DataFrame列名的字符串，在DataFrame上调用get_dummies时，必须传递一个长度等于列数的列表。**

​	**当传递的是字典，字典的键是DataFrame的原列名，值是要加的前缀**

**③prefix_sep：str，默认 '_'**

​	**前缀分隔符**

**④dummy_na：bool，默认False**

​	**如果为True，则会新增一列名为`NaN`的列，来表示缺失值，否则忽略data中的缺失值**

**⑤columns：类列表，默认None**

​	**指定哪些列要被转换成虚拟变量，如果`columns = None`，则数据类型为object，string或category的列均被转换**

**⑥sparse：bool，默认False**

​	**虚拟编码列是否应由`SparseArray`(True)或常规NumPy数组（False）支持**

**⑦drop_first：bool，默认False**

​	**是否通过删除第一个级别来从k个分类级别中获取`k - 1`个虚拟变量**

**⑧dtype：dtype，默认布尔值**

​	**新列的数据类型，仅允许一种类型**



| 返回值： |
| -------- |

**:arrow_right:DataFrame**

​	**虚拟编码的数据，如果data中包含不能虚拟编码的其他列，则这些列会原封不动的添加到结果中**





```python
# 1、输入的data是一维数组
----------------------------------------------------------------------------------------------------
s = pd.Series(['foo', 'q', 'bar', 'q', 'bait', 'q', np.nan])
print(pd.get_dummies(s))
print("=====================dummy_na = True 此时缺失值也算虚拟变量========================")
print(pd.get_dummies(s, dummy_na=True))


#输出结果如下
    bait    bar    foo      q
0  False  False   True  False
1  False  False  False   True
2  False   True  False  False
3  False  False  False   True
4   True  False  False  False
5  False  False  False   True
6  False  False  False  False
=====================dummy_na = True 此时缺失值也算虚拟变量========================
    bait    bar    foo      q    NaN
0  False  False   True  False  False
1  False  False  False   True  False
2  False   True  False  False  False
3  False  False  False   True  False
4   True  False  False  False  False
5  False  False  False   True  False
6  False  False  False  False   True



# 2、输入的data是Series
----------------------------------------------------------------------------------------------------
ser = pd.Series(list("abcdeade"))
print("=====================普通的get_dummies========================")
print(pd.get_dummies(ser))
print("=====================生成的DataFrame的列名加前缀========================")
print(pd.get_dummies(ser, prefix='col'))
print("=====================生成的DataFrame的列名加前缀，并指定前缀分隔符为 ‘-’========================")
print(pd.get_dummies(ser, prefix='col', prefix_sep='-'))
print("=====================将结果转成0/1矩阵========================")
print(pd.get_dummies(ser, dtype=np.uint8))
print("=====================将结果转成0/1矩阵,不保留第一个分类========================")
print(pd.get_dummies(ser, drop_first=True, dtype=np.uint8))


#输出结果如下
=====================普通的get_dummies========================
       a      b      c      d      e
0   True  False  False  False  False
1  False   True  False  False  False
2  False  False   True  False  False
3  False  False  False   True  False
4  False  False  False  False   True
5   True  False  False  False  False
6  False  False  False   True  False
7  False  False  False  False   True
=====================生成的DataFrame的列名加前缀========================
   col_a  col_b  col_c  col_d  col_e
0   True  False  False  False  False
1  False   True  False  False  False
2  False  False   True  False  False
3  False  False  False   True  False
4  False  False  False  False   True
5   True  False  False  False  False
6  False  False  False   True  False
7  False  False  False  False   True
=====================生成的DataFrame的列名加前缀，并指定前缀分隔符为 ‘-’========================
   col-a  col-b  col-c  col-d  col-e
0   True  False  False  False  False
1  False   True  False  False  False
2  False  False   True  False  False
3  False  False  False   True  False
4  False  False  False  False   True
5   True  False  False  False  False
6  False  False  False   True  False
7  False  False  False  False   True
=====================将结果转成0/1矩阵========================
   a  b  c  d  e
0  1  0  0  0  0
1  0  1  0  0  0
2  0  0  1  0  0
3  0  0  0  1  0
4  0  0  0  0  1
5  1  0  0  0  0
6  0  0  0  1  0
7  0  0  0  0  1
=====================将结果转成0/1矩阵,不保留第一个分类========================
   b  c  d  e
0  0  0  0  0
1  1  0  0  0
2  0  1  0  0
3  0  0  1  0
4  0  0  0  1
5  0  0  0  0
6  0  0  1  0
7  0  0  0  1



# 3、输入的data是DataFrame
----------------------------------------------------------------------------------------------------
df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})
print("=================原DataFrame=================")
print(df)
print("===========默认情况下，object、string或categorical类型的列才会被编码为虚拟变量，所以 C 列没有被编码================")
print(pd.get_dummies(df, prefix=['col1', 'col2']))
print("===========指定只对 A 列编码成虚拟变量，则pandas会自动添加前缀================")
print(pd.get_dummies(df, columns=['A']))


#输出结果如下
=================原DataFrame=================
   A  B  C
0  a  b  1
1  b  a  2
2  a  c  3
===========默认情况下，object、string或categorical类型的列才会被编码为虚拟变量，所以 C 列没有被编码================
   C  col1_a  col1_b  col2_a  col2_b  col2_c
0  1    True   False   False    True   False
1  2   False    True    True   False   False
2  3    True   False   False   False    True
===========指定只对 A 列编码成虚拟变量，则pandas会自动添加前缀================
   B  C    A_a    A_b
0  b  1   True  False
1  a  2  False   True
2  c  3   True  False



# 4、prefix可以传str，list(长度必须和可编码的列长度相同)和字典(col -> prefix)
----------------------------------------------------------------------------------------------------
df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})
>>> print(pd.get_dummies(df, prefix='col'))
   C  col_a  col_b  col_a  col_b  col_c
0  1   True  False  False   True  False
1  2  False   True   True  False  False
2  3   True  False  False  False   True



df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})
>>> print(pd.get_dummies(df, prefix=['col1', 'col2']))		#给每个分类的列加一个前缀
   C  col1_a  col1_b  col2_a  col2_b  col2_c
0  1    True   False   False    True   False
1  2   False    True    True   False   False
2  3    True   False   False   False    True



df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})
>>> print(pd.get_dummies(df, prefix={'B': 'col_B', 'A': 'ace'}))
   C  ace_a  ace_b  col_B_a  col_B_b  col_B_c
0  1   True  False    False     True    False
1  2  False   True     True    False    False
2  3   True  False    False    False     True
```



**与pd.cut联用**

```python
values = np.random.uniform(0, 1, 10)
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
print("===========生成的数组==================")
print(values)
print("===============标记每个数值的所在的区间，即所在的分箱=====================")
print(pd.get_dummies(pd.cut(values, bins), dtype=np.uint8))


#输出结果如下
===========生成的数组==================
[0.19317033 0.2936925  0.81792751 0.55948738 0.67792545 0.80912668
 0.86857215 0.41799246 0.05893816 0.478459  ]
===============标记每个数值的所在的区间，即所在的分箱=====================
   (0.0, 0.2]  (0.2, 0.4]  (0.4, 0.6]  (0.6, 0.8]  (0.8, 1.0]
0           1           0           0           0           0
1           0           1           0           0           0
2           0           0           0           0           1
3           0           0           1           0           0
4           0           0           0           1           0
5           0           0           0           0           1
6           0           0           0           0           1
7           0           0           1           0           0
8           1           0           0           0           0
9           0           0           1           0           0
```





**一个很清晰的显示，它表示每个数据存在于哪个分类**

```python
movie = ["Comedy", "Drama", "Action", "Romantic", "Crime", "Thriller"]
np.random.seed(123)
N = 10

# 制造一些样本，比如每个电影的分类是什么 其index是RangeIndex, value为分类名，一个电影可能有好几个分类
def make_sample():
    x = np.random.randint(1, 4)
    return ",".join(np.random.choice(movie, x))

movie_info = pd.DataFrame({'id': range(N), 'movie': [make_sample() for _ in range(N)]})
print("=============movie_info,DataFrame================")
print(movie_info)
print("=============DataFrame的拼接，movie列式其分类名，后面是他们的虚拟编码================")
new_df = movie_info['movie'].str.get_dummies(',')
print(movie_info[['movie']].join(new_df))


#输出结果如下
=============movie_info,DataFrame================
   id                  movie
0   0  Thriller,Action,Crime
1   1  Drama,Romantic,Action
2   2           Drama,Comedy
3   3           Drama,Comedy
4   4  Comedy,Drama,Romantic
5   5  Thriller,Crime,Comedy
6   6                  Crime
7   7        Romantic,Action
8   8                 Action
9   9                 Comedy
=============DataFrame的拼接，movie列式其分类名，后面是他们的虚拟编码================
                   movie  Action  Comedy  Crime  Drama  Romantic  Thriller
0  Thriller,Action,Crime       1       0      1      0         0         1
1  Drama,Romantic,Action       1       0      0      1         1         0
2           Drama,Comedy       0       1      0      1         0         0
3           Drama,Comedy       0       1      0      1         0         0
4  Comedy,Drama,Romantic       0       1      0      1         1         0
5  Thriller,Crime,Comedy       0       1      1      0         0         1
6                  Crime       0       0      1      0         0         0
7        Romantic,Action       1       0      0      0         1         0
8                 Action       1       0      0      0         0         0
9                 Comedy       0       1      0      0         0         0
```





### pandas.from_dummies

**==pandas.from_dummies(*data, sep=None, default_category=None*)==**

​	**从虚拟编码的DataFrame中创建一个可分类的DataFrame，是`pandas.get_dummies()`的逆操作.**

​	**传递的虚拟数据的列应该只包含 1 和 0，或者布尔值**



| 参数： |
| ------ |

**①data：DataFrame**

​	**虚拟编码为0/1形式的数据**

**②sep：str，默认None**

​	**虚拟编码列名中使用的分隔符，用于分隔类别名称和前缀。例如，如果列名为`prefix_A`和`prefix_B`，则可以通过指定`sep='_'`来去除下划线**

**③default_category：None，Hashable 或 Hashables的字典，默认None**

​	**当原数据一行中所有的虚拟变量为0/False时，它会被指定为默认分类值。这个参数值可以是单一值，也可以是字典**



| 返回值： |
| -------- |

**:arrow_right:DataFrame**





```python
df = pd.DataFrame({"a": [1, 0, 0, 1], "b": [0, 1, 0, 0],
                   "c": [0, 0, 1, 0]})
print("=============原DataFrame===============")
print(df)
print("=============从虚拟编码的DataFrame转换成原来的样子===============")
print(pd.from_dummies(df))


#输出结果如下
=============原DataFrame===============
   a  b  c
0  1  0  0
1  0  1  0
2  0  0  1
3  1  0  0
=============从虚拟编码的DataFrame转换成原来的样子===============
    
0  a
1  b
2  c
3  a


----------------------------------------------------------------------------------------------------

df = pd.DataFrame({"col1_a": [1, 0, 1], "col1_b": [0, 1, 0],
                   "col2_a": [0, 1, 0], "col2_b": [1, 0, 0],
                   "col2_c": [0, 0, 1]})
print("=============原DataFrame===============")
print(df)
print("=============指定分隔符为 '_' ===============")
print(pd.from_dummies(df, sep='_'))


#输出结果如下
=============原DataFrame===============
   col1_a  col1_b  col2_a  col2_b  col2_c
0       1       0       0       1       0
1       0       1       1       0       0
2       1       0       0       0       1
=============指定分隔符为 '_' ===============
  col1 col2
0    a    b
1    b    a
2    a    c

----------------------------------------------------------------------------------------------------

df = pd.DataFrame({"col1_a": [1, 0, 0], "col1_b": [0, 1, 0],
                   "col2_a": [0, 1, 0], "col2_b": [1, 0, 0],
                   "col2_c": [0, 0, 0]})
print("=============原DataFrame===============")
print(df)
print("=============如果某一列为0/False,则指定默认分类为new===============")
print(pd.from_dummies(df, sep='_', default_category="new"))
print("=============如果某一列为0/False,则通过字典的方式指定每列的默认分类值===============")
print(pd.from_dummies(df, sep='_', default_category={'col1': 'x', 'col2': 'y'}))



#输出结果如下
=============原DataFrame===============
   col1_a  col1_b  col2_a  col2_b  col2_c
0       1       0       0       1       0
1       0       1       1       0       0
2       0       0       0       0       0
=============如果某一列为0/False,则指定默认分类为new===============
  col1 col2
0    a    b
1    b    a
2  new  new
=============如果某一列为0/False,则通过字典的方式指定每列的默认分类值===============
  col1 col2
0    a    b
1    b    a
2    x    y

```





### pandas.Series.str.get_dummies

**==Series.str.get_dummies(*sep='|'*)==**

​	**对于Series，会返回虚拟/指示变量的DataFrame**



| 参数： |
| ------ |

**sep：str，默认"|"**

​	**string的分隔符**





```python
movie = ["Comedy", "Drama", "Action", "Romantic", "Crime", "Thriller"]
np.random.seed(123)
N = 10

# 制造一些样本，比如每个电影的分类是什么 其index是RangeIndex, value为分类名，一个电影可能有好几个分类
def make_sample():
    x = np.random.randint(1, 4)
    return ",".join(np.random.choice(movie, x))

ser = pd.Series([make_sample() for _ in range(N)])
print("=============原Series================")
print(ser)
print("=============虚拟变量的DataFrame================")
print(ser.str.get_dummies(","))



#输出结果如下
=============原Series================
0    Thriller,Action,Crime
1    Drama,Romantic,Action
2             Drama,Comedy
3             Drama,Comedy
4    Comedy,Drama,Romantic
5    Thriller,Crime,Comedy
6                    Crime
7          Romantic,Action
8                   Action
9                   Comedy
dtype: object
=============虚拟变量的DataFrame================
   Action  Comedy  Crime  Drama  Romantic  Thriller
0       1       0      1      0         0         1
1       1       0      0      1         1         0
2       0       1      0      1         0         0
3       0       1      0      1         0         0
4       0       1      0      1         1         0
5       0       1      1      0         0         1
6       0       0      1      0         0         0
7       1       0      0      0         1         0
8       1       0      0      0         0         0
9       0       1      0      0         0         0
```



### :heavy_exclamation_mark:NumPy实现get_dummies的操作 ###

**有几个函数要介绍**

**==numpy.unique(*ar, return_index=False, return_inverse=False, return_counts=False, axis=None, equal_nan=True, sorted=True*)==**

​	**返回唯一元素的数组**



| 参数： |
| ------ |

**①ar：array_like**

​	**输出数组，如果axis未指定，则会将输入数组展平**

**②return_index：bool，可选**

​	**如果为真，会返回唯一元素在ar中第一次出现的索引**

**③return_inverse: bool,可选**

​	**如果为True，返回数组ar在唯一数组中的索引，这些索引可以用来重建ar**

**④return_counts：bool，可选**

​	**如果为True，则返回每个唯一项在ar中出现的次数**

**⑤axis：int 或 None，可选**

​	**指定沿着哪个轴查找唯一值，如果为None，则ar将被展平**

**⑥equal_nan：bool，可选**

​	**如果为True，将返回数组中的多个NaN值合并为一个**

**⑦sorted：bool，可选**

​	**如果为True，则返回的唯一数组一定会被排序；如果为False，则返回的唯一数组的顺序不稳定**



| 返回值： |
| -------- |

**:arrow_right:unique：ndarray**

​	**返回唯一值的数组**

**:arrow_right:unique_indics：ndarray，可选**

​	**如果return_index为True，则返回此数组，里面存的是唯一值在原数组中首次出现的索引**

**:arrow_right:unique_inverse：ndarray，可选**

​	**如果return_inverse为True，则此索引可用于重建数组**

**:arrow_right:unique_counts：ndarray，可选**

​	**如果return_counts为True，则返回此数组，数组中存的是每个唯一值在原数组中出现的次数**



```python
arr = [1, 1, 2, 5, 1, 1, 2, 3]
print("===============原数组======================")
print(arr)
print("===================返回第一次出现唯一元素的索引============================")
print(np.unique(arr, return_index=True))
print("===================返回唯一元素在arr中出现的次数============================")
print(np.unique(arr, return_counts=True))
print("===================返回arr在唯一数组中出现的索引，用于重建数组============================")
print(np.unique(arr, return_inverse=True))
unique_arr, idx = np.unique(arr, return_inverse=True)
print("=============重塑数组================")
print(unique_arr[idx])


#输出结果如下
===============原数组======================
[1, 1, 2, 5, 1, 1, 2, 3]
===================返回第一次出现唯一元素的索引============================
(array([1, 2, 3, 5]), array([0, 2, 7, 3], dtype=int64))
===================返回唯一元素在arr中出现的次数============================
(array([1, 2, 3, 5]), array([4, 2, 1, 1], dtype=int64))
===================返回arr在唯一数组中出现的索引，用于重建数组============================
(array([1, 2, 3, 5]), array([0, 0, 1, 3, 0, 0, 1, 2], dtype=int64))
=============重塑数组================
[1 1 2 5 1 1 2 3]
```





**==numpy.concatenate(*(a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind"*)==**

​	**沿着存在的轴将多个数组加入到一个序列。**

​	**当要连接的数组中有一个或多个是MaskArray时，此函数将返回一个MaskArray对象而不是ndarray，但输入的掩码不会被保留。这时，使用`numpy.ma.concatenate`是更好的选择**



| 参数： |
| ------ |

**①a1, a2, ... ：数组的序列**

​	**指定需要连接哪些数组，数组必须具有相同的形状，除了对应于axis的维度**

**②axis：int，可选，默认0**

​	**沿着哪个轴连接数组，如果`axis = None`，则在连接之前将数组展平**

**③out：ndarray，可选**

​	**如果提供，则结果数组传到out所指定的数组中，否则返回新的ndarray**

**④dtype：str 或 dtype**

​	**如果提供，结果数组将具有此数据类型。注意，此参数不能与out一起提供**

**⑤casting：{'no', 'equiv', 'safe', 'same_kind', 'unsafe'}，可选**

​	**控制可能发生的数据类型转换，默认`same_kind`**



| 返回值： |
| -------- |

**:arrow_right:返回ndarray，连接后的数组**



```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
>>> np.concatenate((a, b), axis=0)
array([[1, 2],
       [3, 4],
       [5, 6]])

>>> np.concatenate((a, b.T), axis=1)
array([[1, 2, 5],
       [3, 4, 6]])

>>> np.concatenate((a, b), axis=None)
array([1, 2, 3, 4, 5, 6])
```





**对于数据量大的数据来说，用str.get_dummies方法创建多成员虚拟向量的速度不是那么快，所以可以使用NumPy来实现其操作**

​	**具体实现如下：（重点关注第二步和第三步，以及第四步的写入数据）**

```python
# 1 模拟十万行多标签列
N = 100000
tags_pool = np.array(
    ["music", "dance", "edu", "game", "tech",
     "food", "pet", "travel", "comedy", "sport"]
)
rng = np.random.default_rng(42)

# 每行随机 1~3 个标签，用 "|" 连接
def make_sample():
    k = rng.integers(1, 4)                 # 标签数
    return "|".join(rng.choice(tags_pool, k, replace=False))
col = pd.Series([make_sample() for _ in range(N)], name="tags")
col.head()


#  2 拆分为一维标签数组 + 行号数组
split_lists = col.str.split("|")           # Series[list[str]]
lens = split_lists.str.len().to_numpy()    # 每个数据有几个分类
row_idx = np.repeat(np.arange(N), lens)    # 第x个数据有n个分类就重复n次，表示x有n个分类要标记
row_idx[:1000]
flat_tags  = np.concatenate(split_lists.to_numpy())  # 把所有的分类都摊开
print(flat_tags)

# 3) 建立“标签 → 整数”映射
# np.unique([1,3,5,2,2], return_inverse=True)
uniques, tag_pos = np.unique(flat_tags, return_inverse=True)
# uniques      : 所有不重复的分类
# tag_pos      : 分类展平的数组在 唯一分类列表 （unique）中的位置，也表示 每个分类 是什么（只不过现在是0 —— n-1 编码n个分类）



# 4 写入 NumPy 0/1 矩阵
n_rows, n_cols = N, len(uniques)        #这里列使用uniques的长度是因为随机抽取可能取不到 tags_pool 里的所有数据
onehot = np.zeros((n_rows, n_cols), dtype=np.uint8)     #构造全0矩阵
onehot[row_idx, tag_pos] = 1            # 接21行，现在 少一个 分类值，整行的标记是[0, 1] [0, 2] [1, 5]... 第一个值代表第几个数据，第二个值代表第几个分类

# 5 把uniques 封装为 DataFrame
df_dummies = pd.DataFrame(onehot, columns=uniques, index=col.index)
df_dummies.head(10)
```







## #其他函数

### Series.isin

**==Series.isin(*values*)==**

​	**判断Series中的元素是否包含在values中，返回一个布尔的Series**

| 参数： |
| ------ |

**values: set 或 list**

​	**values的序列，传入单个字符串将引发`TypeError`，必须包装成列表**



```python
>>> s = pd.Series(['llama', 'cow', 'llama', 'beetle', 'llama',
...                'hippo'], name='animal')
>>> s.isin(['cow', 'llama'])
0     True
1     True
2     True
3    False
4     True
5    False
Name: animal, dtype: bool


# 使用 `~` 反转布尔值，取逻辑非
>>> ~s.isin(['cow', 'llama'])
0    False
1    False
2    False
3     True
4    False
5     True
Name: animal, dtype: bool


#字符串和整数不同，所以无法比较
>>> pd.Series([1]).isin(['1'])
0    False
dtype: bool
>>> pd.Series([1.1]).isin(['1.1'])
0    False
dtype: bool


#传入一个字符串，引发TypeError
>>> s = pd.Series(['llama', 'cow', 'llama', 'beetle', 'llama',
...               'hippo'], name='animal')
>>> s.isin('llama')
TypeError: only list-like objects are allowed to be passed to isin(), you passed a `str`
```





### DataFrame.isin

**==DataFrame.isin(*values*)==**

​	**判断DataFrame的每个元素是否包含在values中，返回布尔值的DataFrame**



| 参数： |
| ------ |

**values：iterable, Series, DataFrame 或dict**

​	**只有当所有标签匹配时，结果才会在某个位置为True。**

- **如果values是一个Series，则该位置是索引**
- **如果values是一个dict，则键必须是列名，值是对应的values**
- **如果values是一个DataFrame，则索引和列标签都必须匹配**



```python
df = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]},
                  index=['falcon', 'dog'])
print("===============原DataFrame==================")
print(df)
print("===============values = iterable,判断是否在[0, 2, 5]中==================")
print(df.isin([0, 2, 5]))
print("===============values = iterable,判断是否不在[0, 2, 5]中，取反`~`==================")
print(~df.isin([0, 2, 5]))
print("===============values = Series==================")
print(df.isin(pd.Series([2, 2], index=['falcon', 'dog'])))
print("===============values = dict==================")
print(df.isin({'num_legs': np.arange(5), 'num_wings': [-1, 0, 5]}))
compare_df = pd.DataFrame({'num_legs': [5, 3, 5], 'num_wings': [2, 0, 5]},
                  index=['falcon', 'dog', 'cat'])
print("===============values = DataFrame==================")
print(df.isin(compare_df))



#输出结果如下
===============原DataFrame==================
        num_legs  num_wings
falcon         2          2
dog            4          0
===============values = iterable,判断是否在[0, 2, 5]中==================
        num_legs  num_wings
falcon      True       True
dog        False       True
===============values = iterable,判断是否不在[0, 2, 5]中，取反`~`==================
        num_legs  num_wings
falcon     False      False
dog         True      False
===============values = Series==================
        num_legs  num_wings
falcon      True       True
dog        False      False
===============values = dict==================
        num_legs  num_wings
falcon      True      False
dog         True       True
===============values = DataFrame==================
        num_legs  num_wings
falcon     False       True
dog        False       True
```





### Series/Index/pandas.unique

**==pandas.unique(*values*)==**

​	**根据哈希表返回唯一值，按出现的顺序返回唯一值，不进行排序，包括NA值**

​	**对于足够长的序列，速度明显快于numpy.unique**

| 参数： |
| ------ |

**values: 一维array_like**



| 返回值: |
| ------- |

**:arrow_right:numpy.ndarray 或 ExtensionArray**

- **Index：当输入是Index**
- **Categorical对象：当输入是分类数据类型时**
- **ndarray：当输入是Series/ndarray**



```python
#一般的ndarray
>>> pd.unique(pd.Series([2, 1, 3, 3]))
array([2, 1, 3])

>>> pd.unique(pd.Series([2] + [1] * 5))
array([2, 1])

>>> pd.unique(pd.Series([2, 1, 3, 3, np.nan]))
array([ 2.,  1.,  3., nan])				#包含了缺失值


#看元组的唯一性
>>> pd.unique(pd.Series([("a", "b"), ("b", "a"), ("a", "c"), ("b", "a")]).values)
array([('a', 'b'), ('b', 'a'), ('a', 'c')], dtype=object)



#扩展数据类型
>>> pd.unique(pd.Series([pd.Timestamp("20160101"), pd.Timestamp("20160101")]))
array(['2016-01-01T00:00:00.000000000'], dtype='datetime64[ns]')

>>> pd.unique(
...     pd.Series(
...         [
...             pd.Timestamp("20160101", tz="US/Eastern"),
...             pd.Timestamp("20160101", tz="US/Eastern"),
...         ]
...     )
... )
<DatetimeArray>
['2016-01-01 00:00:00-05:00']
Length: 1, dtype: datetime64[ns, US/Eastern]

>>> pd.unique(
...     pd.Index(
...         [
...             pd.Timestamp("20160101", tz="US/Eastern"),
...             pd.Timestamp("20160101", tz="US/Eastern"),
...         ]
...     )
... )
DatetimeIndex(['2016-01-01 00:00:00-05:00'],
        dtype='datetime64[ns, US/Eastern]',
        freq=None)




#Categorical数据类型
#无序的分类按出现顺序返回
>>> pd.unique(pd.Series(pd.Categorical(list("baabc"))))
['b', 'a', 'c']
Categories (3, object): ['a', 'b', 'c']


#有序的分类保留了类别排序['a' < 'b' < 'c']
>>> pd.unique(
...     pd.Series(
...         pd.Categorical(list("baabc"), categories=list("abc"), ordered=True)
...     )
... )
['b', 'a', 'c']
Categories (3, object): ['a' < 'b' < 'c']
```







### Index.get_indexer

**==Index.get_indexer(*target, method=None, limit=None, tolerance=None*)==**

​	**根据当前索引计算target的索引器和掩码**



| 参数： |
| ------ |

**①target：索引**

**②method: {None, 'pad/ffill', 'backfill/bfill', 'nearest'}， 可选**

​	**默认为None，精确匹配**

**③limit: int，可选**

​	**`target`用于匹配不精确匹配的最大连续标签数**

**④tolerance：可选**

​	**容差，满足`abs(index[indexer] - target) <= tolerance`，可以是标量，也可以是列表**



| 返回值： |
| -------- |

**:arrow_right:np.ndarray：0到$n - 1$之间的整数，对于不匹配的值返回`-1`**



```python
>>> index = pd.Index(['c', 'a', 'b'])
>>> index.get_indexer(['a', 'b', 'x'])
array([ 1,  2, -1])					#a对应的索引为1，b对应的索引为2，不存在的为-1
```







# # plot绘图

## :a:对于Series

```python
>>> ser = pd.Series([1, 2, 3, 3])
>>> plot = ser.plot(kind='hist', title="My plot")
```



<img src="G:\01资料\Pictures\pandas-DataFrame-plot-1.png" style="zoom:80%;" />



## :b:对于DataFrame

```python
>>> df = pd.DataFrame({'length': [1.5, 0.5, 1.2, 0.9, 3],
...                   'width': [0.7, 0.2, 0.15, 0.2, 1.1]},
...                   index=['pig', 'rabbit', 'duck', 'chicken', 'horse'])
>>> plot = df.plot(title="DataFrame Plot")
```



<img src="G:\01资料\Pictures\pandas-DataFrame-plot-2.png" style="zoom:80%;" />

















