#import <stdio.h>
#import <string.h>
#include <openssl/crypto.h>
#include <openssl/ssl.h>
#include "unhex.h"

// cc hash.c -I/usr/local/Cellar//openssl@1.1/1.1.0h/include/ -L/usr/local/Cellar//openssl@1.1/1.1.0h/lib -lcrypto

char pnr[] = "somesalt000000-0000";
const int salt_len = 8;
int main(int argc, char *argv[]) {
    long c = 0;
    int digit0 = atoi(argv[1]);
    int digit1 = atoi(argv[2]);
    unsigned char *data;
    hexs2bin(argv[3], &data);

    // Generate all pnrs
    for (int d0 = digit0; d0 < digit0 + 1; d0++) { // First digit of pnr
        for (int d1 = digit1; d1 < digit1 + 1; d1++) { // Second digit of pnr
            for (int d2 = 0; d2 < 2; d2++) { // ...
                for (int d3 = 0; d3 < 10; d3++) {
                    for (int d4 = 0; d4 < 10; d4++) {
                        for (int d5 = 0; d5 < 4; d5++) {
                            for (int d6 = 0; d6 < 10; d6++) {
                                for (int d7 = 0; d7 < 10; d7++) {
                                    for (int d8 = 0; d8 < 10; d8++) {
                                        for (int d9 = 0; d9 < 10; d9++) {
                                            c++;
                                            const unsigned char *hash;

                                            pnr[salt_len + 0] = '0' + d0;
                                            pnr[salt_len + 1] = '0' + d1;
                                            pnr[salt_len + 2] = '0' + d2;
                                            pnr[salt_len + 3] = '0' + d3;
                                            pnr[salt_len + 4] = '0' + d4;
                                            pnr[salt_len + 5] = '0' + d5;
                                            // pnr[salt_len + 6] = '-'
                                            pnr[salt_len + 7] = '0' + d6;
                                            pnr[salt_len + 8] = '0' + d7;
                                            pnr[salt_len + 9] = '0' + d8;
                                            pnr[salt_len + 10] = '0' + d9;

                                            hash = SHA256((unsigned const char*)pnr, salt_len + 11, NULL);

                                            if (memcmp(data, hash, SHA256_DIGEST_LENGTH) == 0) {
                                                printf("SHA256(\"%s\") = %s (guess #%ld)\n", pnr, argv[1], c);
                                                return 0;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

