def compute_framebuffer_scale(window_size, frame_buffer_size):
    win_width, win_height = window_size
    fb_width, fb_height = frame_buffer_size

    if win_width != 0 and win_width != 0:
        return fb_width / win_width, fb_height / win_height

    return 1., 1.
