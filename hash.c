#include <stdio.h>
#include <openssl/crypto.h>
#include <openssl/ssl.h>
#include <string.h>

// cc hash.c -I/usr/local/Cellar//openssl@1.1/1.1.0h/include/ -L/usr/local/Cellar//openssl@1.1/1.1.0h/lib -lcrypto

char hex[65];
int main(int argc, char* argv[]) {
    const unsigned char *hash = SHA256((const unsigned char*)argv[1], strlen(argv[1]), NULL);
    int i = 0;
    for(i = 0; i < SHA256_DIGEST_LENGTH; i++)
    {
        sprintf(hex + (i * 2), "%02x", hash[i]);
    }
    hex[64] = 0;
    puts(hex);
    return 0;
}
