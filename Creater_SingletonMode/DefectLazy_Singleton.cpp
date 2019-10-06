#include <iostream>
// version1:
// with problems below:
// 1. thread is not safe
// 2. memory leak

class Singleton{
private:
    /*构造函数私有化*/
    Singleton() { std::cout<<"constructor called!"<<std::endl; }

    /*禁止赋值和拷贝*/
    Singleton(Singleton&)=delete;
    Singleton& operator=(const Singleton&)=delete;

    /*静态成员*/
    static Singleton* m_instance_ptr;
public:
    ~Singleton() { std::cout<<"destructor called!"<<std::endl; }

    /*通过接口获取实例*/
    static Singleton* get_instance() {
        if(m_instance_ptr==nullptr)  
            m_instance_ptr = new Singleton;
        return m_instance_ptr;
    }
    void use() const { std::cout << "in use" << std::endl; }
};

/*类静态成员初始化*/
Singleton* Singleton::m_instance_ptr = nullptr;

int main(){
    Singleton* instance = Singleton::get_instance();
    Singleton* instance_2 = Singleton::get_instance();
    return 0;
}

