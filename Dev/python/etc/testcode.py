# -*- coding : UTF-8 -*-
#アンダースコアの使用方法について
#数字を読みやすくする様にアンダースコアを数字内に加える事が出来ます。一般で使われてる3桁ごとにカンマを実現
import sys
import os
class Test:
    def __init__(self,*args):
        self.args = args

    #①通常の関数定義
    def test(self):
        result = int(sys.argv[1]) + int(sys.argv[2])
        return result,sys.argv[1],sys.argv[2]
    
    #②プライベート属性的な関数定義
    #Private属性のような関数を定義できて内部的に扱える。
    #from M import * の時、では一つのアンダースコアで始まる関数はインポートされませんが、class内の関数だとclassx._func()で関数を呼ぶ事が出来ます。
    def _test(self):
        result = int(sys.argv[1]) + int(sys.argv[2])
        return result, sys.argv[1], sys.argv[2]
    
    #③重要関数
    #Python内の重要関数と名付けを被らせないために使用をする。
    def test_(self):
        result = int(sys.argv[1]) + int(sys.argv[2])
        return result, sys.argv[1], sys.argv[2]
      
    #④マングリング機構を呼び出す関数定義
    #擬似的にPrivate属性を作れ
    #class内の関数前に二つアンダースコア付けることで、名前の マングリング機構を呼び出します。ここのマングリングとは、インタプリタやコンパイラーが普通の方法で変数を扱わなくなる事
    def __test(self):
        result = int(sys.argv[1]) + int(sys.argv[2])
        return result, sys.argv[1], sys.argv[2]
      
    #⑤class内の関数の前後に二つずつアンダースコア付けることで、magic method
    def __test__(self):
        pass
      
      
if __name__ == "__main__":
    test1 = Test(sys.argv[1], sys.argv[2])
    x,_,z = test1.test()
    print(x,end=",")
    print(z)
    test2 = Test(sys.argv[1], sys.argv[2])
    result2 = test2._test()
    print("{},{},{}".format(result2[0],result2[1],result2[2]))

    test3 = Test(sys.argv[1], sys.argv[2])
    result3 = test3.test_()
    print("{},{},{}".format(result3[0],result3[1],result3[2]))
    
    test4 = Test(sys.argv[1],sys.argv[2])
    result4 = test4._Test__test()
    print("{},{},{}".format(result4[0],result4[1],result4[2]))
