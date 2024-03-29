#ifndef SRC_COMMON_H_
#define SRC_COMMON_H_

#define NAPI_CALL(env, the_call)                                \
  do {                                                          \
    if ((the_call) != napi_ok) {                                \
      const napi_extended_error_info *error_info;               \
      napi_get_last_error_info((env), &error_info);             \
      bool is_pending;                                          \
      const char* err_message = error_info->error_message;      \
      napi_is_exception_pending((env), &is_pending);            \
      if (!is_pending) {                                        \
        const char* error_message = err_message != NULL ?       \
          err_message :                                         \
          "empty error message";                                \
        napi_throw_error((env), NULL, error_message);           \
      }                                                         \
      return NULL;                                              \
    }                                                           \
  } while (0)

#endif

#if !defined(__wasm__) || ((defined(__EMSCRIPTEN__) && defined(__EMSCRIPTEN_PTHREADS__)) || (defined(__wasi__) && defined(_REENTRANT)))
#define HAVE_THREADS
#endif

#ifdef __cplusplus
#define EXTERN_C extern "C"
#else
#define EXTERN_C
#endif
