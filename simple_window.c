// Taken from https://stackoverflow.com/questions/41190343/how-to-display-an-image-without-decorations?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa#comment69659775_41228386
// simple_window (compile with `gcc -L/usr/X11R6/lib -lX11 -o simple_window simple_window.c')
#include <stdio.h>
#include <X11/Xlib.h>

int main(int argc, const char * argv[]) {
    Display * root;
    Window win;
    int screen;
    root = XOpenDisplay(NULL);
    screen = DefaultScreen(root);
    Display* display = XOpenDisplay(NULL);

    XVisualInfo vinfo;
    XMatchVisualInfo(display, DefaultScreen(display), 32, TrueColor, &vinfo);

    XSetWindowAttributes attr;
    attr.colormap = XCreateColormap(display, DefaultRootWindow(display), vinfo.visual, AllocNone);
    attr.border_pixel = 0;
    attr.background_pixel = 0;
    win = XCreateSimpleWindow(display,
                              RootWindow(root, screen),
                              10, 10,
                              400, 600,
                              0,
                              BlackPixel(root, screen),
                              WhitePixel(root, screen));
    Atom win_type = XInternAtom(root, "_NET_WM_WINDOW_TYPE", False);
    long value = XInternAtom(root, "_NET_WM_WINDOW_TYPE_DOCK", False);
    XChangeProperty(root,
                    win,
                    win_type,
                    4, 32,
                    PropModeReplace,
                    (unsigned char *) &value, 1);
    XMapWindow(root, win);
    printf("Window created %lu\n", win);
    XEvent e;
    while(1) {
        XNextEvent(root, &e);
        if (e.type == KeyPress) {
            break;
        }
    }
    XCloseDisplay(root);
    return 0;
}
