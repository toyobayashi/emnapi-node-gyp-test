#include "./common.h"

#ifdef HAVE_THREADS

#include <napi.h>
#include <chrono>
#include <thread>

using namespace Napi;

class EchoWorker : public Napi::AsyncProgressQueueWorker<uint32_t> {
 public:
  EchoWorker(Function& okCallback,
             Function& progressCallback,
             std::string& echo)
      : AsyncProgressQueueWorker(okCallback), echo(echo) {
    this->progressCallback.Reset(progressCallback, 1);
  }

  void Execute(const ExecutionProgress& progress) {
    for (uint32_t i = 0; i < 6; ++i) {
      std::this_thread::sleep_for(std::chrono::milliseconds(200));
      progress.Send(&i, 1);
    }
  }

  void OnProgress(const uint32_t* data, size_t /* count */) {
    HandleScope scope(Env());

    if (!this->progressCallback.IsEmpty()) {
      this->progressCallback.Call(Receiver().Value(),
                                  {Number::New(Env(), *data)});
    }
  }

  void OnOK() {
    HandleScope scope(Env());
    Callback().Call(Receiver().Value(),
                    {Env().Null(), String::New(Env(), echo)});
  }

  void OnError(const Error& e) {
    HandleScope scope(Env());
    Callback().Call(Receiver().Value(), {e.Value()});
  }

 private:
  std::string echo;
  FunctionReference progressCallback;
};

extern "C" napi_value echo(napi_env env, napi_callback_info i) {
  CallbackInfo info{ env, i };
  std::string in = info[0].As<String>();
  Function okCb = info[1].As<Function>();
  Function progressCb = info[2].As<Function>();
  EchoWorker* wk = new EchoWorker(okCb, progressCb, in);
  wk->Queue();
  return info.Env().Undefined();
}

#else
#include <js_native_api.h>
#endif

extern "C" napi_value echo_sync(napi_env env, napi_callback_info info) {
  size_t argc = 1, len;
  napi_value argv, ret;
  NAPI_CALL(env, napi_get_cb_info(env, info, &argc, &argv, nullptr, nullptr));
  char in[10];
  NAPI_CALL(env, napi_get_value_string_utf8(env, argv, in, 10, &len));
  NAPI_CALL(env, napi_create_string_utf8(env, in, len, &ret));
  return ret;
}
