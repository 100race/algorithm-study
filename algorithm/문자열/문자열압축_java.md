##  문제설명
알파벳 대문자로 이루어진 문자열을 입력받아 같은 문자가 연속으로 반복되는 경우 반복되는 
문자 바로 오른쪽에 반복 횟수를 표기하는 방법으로 문자열을 압축하는 프로그램을 작성하시
오. 단 반복횟수가 1인 경우 생략합니다.

## 입출력 예시
Input: KKHSSSSSSSE <br>

Output: K2HS7E


## 풀이
```java
import java.util.*;
class Main {	
	public String solution(String s){
		String answer="";
		s=s+" ";
		int cnt=1;
		for(int i=0; i<s.length()-1; i++){
			if(s.charAt(i)==s.charAt(i+1)) cnt++;
			else{
				answer+=s.charAt(i);
				if(cnt>1) answer+=String.valueOf(cnt);
				cnt=1;
			}
		}
		return answer;
	}

	public static void main(String[] args){
		Main T = new Main();
		Scanner kb = new Scanner(System.in);
		String str=kb.next();
		System.out.println(T.solution(str));
	}
}
```
- 아주 쉬운 문젠데 이렇게 자꾸 검사하는 문제를 prev 로 해결하려 해서 오답확률이 올라간다. prev보다는 i+1 인덱싱을 활용해 다음걸 미리 계산하기로. <br>
또한 필요한 상황에서는 prev으로 검사. java로 문제풀이하는 감은 쓰던거라 바로 익숙해지는 것 같다.
