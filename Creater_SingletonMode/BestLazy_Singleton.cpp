#includes <iostream>

class Singleton {
private:
	Singleton() {
		std::cout << "constructor called!" << std::endl;
	}
	
public:
	~Singleton() {
		std::cout << "Destructor called!" << std::endl;
	}
	
	/*禁止复制和拷贝*/
	Singleton(const Singleton &) = delete;
	Singleton & operator=(const Singleton &) = delete;
	
	/*静态成员属性*/
	static Singleton & get_instance() {
		static Singleton instance;
		return instance;
	}
};

int main()
{
	Singleton & instance_1 = Singleton::get_instance();
	Singleton & instance_2 = Singleton::get_instance();
}

