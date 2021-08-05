## 문제설명
지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다. 각 격자
판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다. 봉우리 지역이 몇 개 
있는 지 알아내는 프로그램을 작성하세요. 
격자의 가장자리는 0으로 초기화 되었다고 가정한다.
만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.

첫 줄에 자연수 N이 주어진다.(2<=N<=50) 
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는
다. 

## 입출력 예시
Input: 5<br>
5 3 7 2 3<br>
3 7 1 6 1<br>
7 2 5 3 4<br>
4 3 6 4 1<br>
8 7 3 5 2 <br>

Output: 10


## 풀이
```java
import java.util.*;
class Main {	
  //2차원배열 4방향검사 - 상,하,좌,우
	int[] dx={-1, 0, 1, 0};
	int[] dy={0, 1, 0, -1};
	public int solution(int n, int[][] arr){
		int answer=0;
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				boolean flag=true;
        //자리 별 4방향 검사 k는 4(4방향)
				for(int k=0; k<4; k++){
					int nx=i+dx[k];
					int ny=j+dy[k];
					if(nx>=0 && nx<n && ny>=0 && ny<n && arr[nx][ny]>=arr[i][j]){ //array 인덱스에러 나올수 있는 부분보다 앞에 검사를 해줘서 index에러를 방지
						flag=false;
						break;
					}
				}
				if(flag) answer++;
			}
		}
		return answer;
	}

	public static void main(String[] args){
		Main T = new Main();
		Scanner kb = new Scanner(System.in);
		int n=kb.nextInt();
		int[][] arr=new int[n][n];
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				arr[i][j]=kb.nextInt();
			}
		}
		System.out.print(T.solution(n, arr));
	}
}
```
- 이차원배열에서 4방향(상하좌우), 또는 8방향(상하좌우대각선) 검사를 할 때의 패턴
- index Error를 방지하기 위해 if문에서 index 조건을 앞에서 검사 (*순서 중요. 뒤에서 검사할시 intdex error발생)
