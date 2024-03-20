#include <node_api.h>
#include "./common.h"

EXTERN_C napi_value echo(napi_env env, napi_callback_info info);
EXTERN_C napi_value echo_sync(napi_env env, napi_callback_info info);

NAPI_MODULE_INIT() {
  napi_value js_echo_sync;

#ifdef HAVE_THREADS
  napi_value js_echo;
  NAPI_CALL(env, napi_create_function(env, "echo", NAPI_AUTO_LENGTH,
                                      echo, NULL, &js_echo));
  NAPI_CALL(env, napi_set_named_property(env, exports, "echo", js_echo));
#endif

  NAPI_CALL(env, napi_create_function(env, "echoSync", NAPI_AUTO_LENGTH,
                                      echo_sync, NULL, &js_echo_sync));
  NAPI_CALL(env, napi_set_named_property(env, exports, "echoSync", js_echo_sync));
  return exports;
}
