##  문제설명
첫째 줄에 문자열 s와 문자 t가 주어진다. 문자열과 문자는 소문자로만 주어진다. 문자열의 길이는 100을 넘지 않는다
각 문자열 s의 문자가 t와 떨어진 거리를 순서대로 출력한다.

## 입출력 예시
Input: teachermode e <br>

Output: 1 0 1 2 1 0 1 2 2 1 0


## 풀이
```java
import java.util.*;
class Main {	
	public int[] solution(String s, char t){
		int[] answer=new int[s.length()];
		int p=1000; //거리
    //첫번째 루프
		for(int i=0; i<s.length(); i++){
			if(s.charAt(i)==t){
				p=0;
				answer[i]=p;
			}
			else{
				p++;
				answer[i]=p;
			}
		}
		p=1000;
    //두번째 루프
		for(int i=s.length()-1; i>=0; i--){
			if(s.charAt(i)==t) p=0;
			else{
				p++;
				answer[i]=Math.min(answer[i], p);
			}
		}
		return answer;
	}

	public static void main(String[] args){
		Main T = new Main();
		Scanner kb = new Scanner(System.in);
		String str=kb.next();
		char c=kb.next().charAt(0);
		for(int x : T.solution(str, c)){
			System.out.print(x+" ");
		}
	}
}
```
- 복잡하게 split, indexOf로만 생각했었음. 차근차근 생각. 두 방향으로 검사할 수 있다.
