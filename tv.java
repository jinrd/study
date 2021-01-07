package jan_03;

public class tv {
	String brand;
	String model;
	int size;
	String color;
	
	// 생성자

	tv(String b , String m){
		System.out.println("브랜드와 모델 초기화");
		brand = b;
		model = m;
	}
	
	tv(String brand , String model , int size){
		System.out.println("브랜드와 모델 사이즈 초기화");
		this.brand = brand;
		this.model = model;
		this.size = size;
	}
	
	tv(String brand , String model , int size,String color){
		System.out.println("브랜드와 모델 사이즈 색상 초기화");
		this.brand = brand;
		this.model = model;
		this.size = size;
		this.color = color;
	}
	
	// 출력 메서드
	void print()
	{
		String str = String.format("brand: %s model: %s size: %d color: %s",
				brand,model,size, color);
		System.out.println(str);				
	}
	
}
