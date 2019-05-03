#include <iostream>
#include <fstream>

using namespace std;

bool m_isRightTouch ;

bool checksavedinstance()
{
		
		bool value ;
		ifstream fio("sample.txt", ios::app ); 
		
		fio >> value ;
		cout<<"from file = "<<value<<endl;	
		
		return value ;	
		
}

void closepopup()
{
	ofstream outfile("sample.txt");
	
	outfile << m_isRightTouch ;
	
}

int main()
{
		
		if(!checksavedinstance()) {
			cout<<"Left Steering Position Value \n ";
			m_isRightTouch = 0;
		}
		else {
			cout<<"Right Steering Position Value \n";
			m_isRightTouch = 1;
		}	
		
		m_isRightTouch = 1;
					
			
		closepopup();
		closepopup();
		closepopup();
				
		return 0;

}
