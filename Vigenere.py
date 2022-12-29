# 根据输入的key生成key列表
def create_keyList(key):
    key_list = []
    for ch in key:
        key_list.append(ord(ch.upper()) - 65) # 借助ASCII码在数字和字母之间转换
    return key_list


# 加密函数
def Encrypt(plaintext, key_list):
    ciphertext = ""

    i = 0
    for value in plaintext:  # 遍历明文
        if 0 == i % len(key_list):
            i = 0
        if value.isalpha():  # 明文是否为字母,如果是,则判断大小写,分别进行加密
            if value.isupper():
                ciphertext += alpha_table[(ord(value) - 65 + key_list[i]) % 26]
                i += 1
            else:
                ciphertext += alpha_table[(ord(value) - 97 + key_list[i]) % 26].lower()
                i += 1
        else:  # 如果密文不为字母,直接添加到密文字符串里
            ciphertext += value
    return ciphertext


# 解密函数
def Decrypt(ciphertext, key_list):
    plaintext = ""
    i = 0
    for value in ciphertext:  # 遍历密文
        if 0 == i % len(key_list):
            i = 0
        if value.isalpha():  # 密文为否为字母,如果是,则判断大小写,分别进行解密
            if value.isupper():
                plaintext += alpha_table[(ord(value) - 65 - key_list[i]) % 26]
                i += 1
            else:
                plaintext += alpha_table[(ord(value) - 97 - key_list[i]) % 26].lower()
                i += 1
        else:  # 如果密文不为字母,直接添加到明文字符串里
            plaintext += value
    return plaintext

# 主函数
def run():
    print("加密输入1,解密输入2:")
    # 输入功能模式编号
    mode = input()
    # 检查是否为非法输入
    while (mode != '1' and mode != '2'):  
        print("选择错误，请重新输入:")
        mode = input()
    print("请输入密钥:")
    key = input()
    # 输入合法性判断
    while (False == key.isalpha()):  
        print("输入有误!密钥为字母,请重新输入:")
        key = input()
    # 创建key_list
    key_list = create_keyList(key)
    if mode == '1':
        # 加密过程
        print("请输入明文:")
        plaintext = input()
        ciphertext = Encrypt(plaintext, key_list)
        print("密文为:\n" % ciphertext)
    else:
        # 解密过程
        print("请输入密文:")
        ciphertext = input()
        plaintext = Decrypt(ciphertext, key_list)
        print("明文为:\n" % plaintext)

if __name__ == '__main__':
    # 所有的字母表
    alpha_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  
    run()