#include <js_native_api.h>
#include "./common.h"

napi_value js_hello(napi_env env, napi_callback_info info) {
  napi_value world = nullptr;
  const char* str = "world";
  NAPI_CALL(env, napi_create_string_utf8(env, str, NAPI_AUTO_LENGTH, &world));
  return world;
}
