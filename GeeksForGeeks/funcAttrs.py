def test_func_attrs():
    test_func_attrs.first = "foo"
    test_func_attrs.second = 4
    print("Fuck") 


#run function so attrs enter NS
test_func_attrs()
print(test_func_attrs.first)
print(test_func_attrs.second)

