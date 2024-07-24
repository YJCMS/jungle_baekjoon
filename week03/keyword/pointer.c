#include <stdio.h>

int main() {
    int x = 10;
    int *ptr = &x;  // ptr은 x의 주소를 저장

    printf("x의 값: %d\n", x);
    printf("x의 주소: %p\n", (void*)&x);
    printf("ptr이 가리키는 주소: %p\n", (void*)ptr);
    printf("ptr이 가리키는 값: %d\n", *ptr);

    *ptr = 20;  // ptr을 통해 x의 값을 변경
    printf("변경 후 x의 값: %d\n", x);

    return 0;
}

// 실행결과

// x의 값: 10
// x의 주소: 0x16cf171b8
// ptr이 가리키는 주소: 0x16cf171b8
// ptr이 가리키는 값: 10
// 변경 후 x의 값: 20