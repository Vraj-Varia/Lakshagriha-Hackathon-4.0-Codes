#include <stdio.h>
#include <string.h>
#define MAX 13  
#define LEN 13  
#define MAX_COLS 13

char palindrome[LEN + 1] = "WASITACATISAW";
char full_palindrome[2 * LEN - 1 + 1];
char grid[MAX][MAX_COLS + 2] = {
    "       W       ",
    "      WAW      ",
    "     WASAW     ",
    "    WASISAW    ",
    "   WASITISAW   ",
    "  WASITATISAW  ",
    " WASITACATISAW ",
    "  WASITATISAW  ",
    "   WASITISAW   ",
    "    WASISAW    ",
    "     WASAW     ",
    "      WAW      ",
    "       W       "
};

int rows = 13;
int cols = MAX_COLS;
int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

int dfs(int r, int c, int index) {
    if (index == strlen(full_palindrome)) {
        return 1;
    }
    int count = 0;
    for (int d = 0; d < 4; ++d) {
        int nr = r + dr[d];
        int nc = c + dc[d];
        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
            if (grid[nr][nc] == full_palindrome[index]) {
                count += dfs(nr, nc, index + 1);
            }
        }
    }
    return count;
}
void main() {
    int i, len = strlen(palindrome);
    strcpy(full_palindrome, palindrome);
    for (i = len - 2; i >= 0; --i) {
        full_palindrome[len + (len - 2 - i)] = palindrome[i];
    }
    full_palindrome[2 * len - 1] = '\0';
    int total_paths = 0;
    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (grid[r][c] == full_palindrome[0]) {
                total_paths += dfs(r, c, 1);
            }
        }
    }
    printf("Total ways to read the palindrome: %d\n", total_paths);
}
