<template>
  <div class="element">
    <div class="div">
      <PlaceholderImage class="placeholder-image" />
      <div class="navigation">
        <div class="overlap">
          <div class="frame-2">
            <div class="overlap-group">
              <div class="group">
                <div class="logo">
                  <div class="text-wrapper-2">Product Manager</div>
                </div>
                <div class="register">
                  <div class="text-wrapper-3">注册</div>
                </div>
              </div>
              <div class="frame-3">
                <input class="frame-32" />
                <input class="frame-32" text="对话" />
                <input class="frame-32" text="配置" />
                <input class="frame-32" text="联系" />
              </div>
              <div class="rectangle" />
            </div>
            <button class="overlap-group-wrapper">
              <div class="div-wrapper">
                <div class="text-wrapper-4">登录</div>
              </div>
            </button>
          </div>
          <img class="subtract" alt="Subtract" src="subtract.svg" />
        </div>
      </div>
      <div class="auto-layout-vertical">
        <div class="auto-layout-vertical-2">
          <div class="auto-layout-vertical-3">
            <div class="text-wrapper-5">Label goes here</div>
            <div class="text-wrapper-6">Best Product Manager</div>
          </div>
          <p class="p">Welcome to Best product manager.</p>
        </div>
        <div class="auto-layout">
          <Button class="style-filled button-instance" style="filled" text="Start now" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "Person",
  components: {
  },
};
</script>

<style>
.element {
  background-color: #f1f5f9;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
}

.element .div {
  background-color: #f1f5f9;
  height: 1080px;
  position: relative;
  width: 1920px;
}

.element .placeholder-image {
  height: 414px !important;
  left: 129px !important;
  position: absolute !important;
  top: 393px !important;
  width: 615px !important;
}

.element .navigation {
  background-color: var(--primary);
  height: 116px;
  left: 0;
  position: absolute;
  top: 0;
  width: 1920px;
}

.element .overlap {
  height: 373px;
  position: relative;
}

.element .frame-2 {
  border-bottom-style: solid;
  border-bottom-width: 1px;
  border-color: var(--secondary);
  height: 116px;
  left: 0;
  overflow: hidden;
  position: absolute;
  top: 0;
  width: 1920px;
}

.element .overlap-group {
  height: 118px;
  left: 91px;
  position: absolute;
  top: 0;
  width: 1430px;
}

.element .group {
  height: 64px;
  left: 0;
  position: absolute;
  top: 27px;
  width: 1430px;
}

.element .logo {
  height: 24px;
  left: 0;
  position: absolute;
  top: 20px;
  width: 270px;
}

.element .text-wrapper-2 {
  color: var(--tertiary);
  font-family: "DM Sans-Bold", Helvetica;
  font-size: 32px;
  font-weight: 700;
  left: 0;
  letter-spacing: 0.15px;
  line-height: 24px;
  position: absolute;
  top: 0;
  white-space: nowrap;
}

.element .register {
  height: 64px;
  left: 1279px;
  position: absolute;
  top: 0;
  width: 153px;
}

.element .text-wrapper-3 {
  color: var(--tertiary);
  font-family: "DM Sans-Bold", Helvetica;
  font-size: 16px;
  font-weight: 700;
  left: 59px;
  letter-spacing: 0.8px;
  line-height: normal;
  position: absolute;
  text-align: center;
  top: 22px;
}

.element .frame-3 {
  align-items: center;
  display: inline-flex;
  left: 578px;
  position: absolute;
  top: 0;
}

.element .frame-32 {
  color: var(--tertiary) !important;
}

.element .rectangle {
  background-color: var(--annotations);
  border-radius: 35px 35px 0px 0px;
  box-shadow: 0px 1px 2.3px #00000040;
  height: 6px;
  left: 615px;
  position: absolute;
  top: 109px;
  width: 50px;
}

.element .overlap-group-wrapper {
  all: unset;
  box-shadow: 1px 1px 3px #00000040;
  box-sizing: border-box;
  height: 39px;
  left: 1525px;
  position: absolute;
  top: 40px;
  width: 127px;
}

.element .div-wrapper {
  background-image: url(./background.png);
  background-size: 100% 100%;
  height: 39px;
  position: relative;
  width: 125px;
}

.element .text-wrapper-4 {
  color: var(--primary);
  font-family: "Alibaba PuHuiTi-Medium", Helvetica;
  font-size: 16px;
  font-weight: 500;
  left: 46px;
  letter-spacing: 0.8px;
  line-height: 21.6px;
  position: absolute;
  top: 8px;
  white-space: nowrap;
}

.element .subtract {
  height: 373px;
  left: 0;
  mix-blend-mode: soft-light;
  position: absolute;
  top: 0;
  width: 224px;
}

.element .auto-layout-vertical {
  align-items: flex-start;
  display: flex;
  flex-direction: column;
  gap: 38.86px;
  left: 777px;
  position: absolute;
  top: 427px;
  width: 991px;
}

.element .auto-layout-vertical-2 {
  align-items: flex-start;
  display: inline-flex;
  flex: 0 0 auto;
  flex-direction: column;
  gap: 25.91px;
  margin-right: -121.45px;
  position: relative;
}

.element .auto-layout-vertical-3 {
  align-items: flex-start;
  display: inline-flex;
  flex: 0 0 auto;
  flex-direction: column;
  gap: 12.95px;
  position: relative;
}

.element .text-wrapper-5 {
  color: var(--primary);
  font-family: "DM Sans-Medium", Helvetica;
  font-size: 34px;
  font-weight: 500;
  letter-spacing: 0.24px;
  line-height: 35.6px;
  margin-top: -1.62px;
  position: relative;
  width: 991px;
}

.element .text-wrapper-6 {
  color: var(--primary);
  font-family: "DM Sans-Bold", Helvetica;
  font-size: 97.2px;
  font-weight: 700;
  letter-spacing: 0.81px;
  line-height: 123.1px;
  position: relative;
  width: 1112.45px;
}

.element .p {
  color: var(--neutral-7);
  font-family: "DM Sans-Regular", Helvetica;
  font-size: 32.4px;
  font-weight: 400;
  letter-spacing: 0.81px;
  line-height: 51.8px;
  position: relative;
  width: 991px;
}

.element .auto-layout {
  align-items: flex-start;
  display: inline-flex;
  flex: 0 0 auto;
  gap: 38.86px;
  position: relative;
}

.element .style-filled {
  background-color: var(--primary) !important;
  border: unset !important;
  border-color: unset !important;
  border-radius: 80.96px !important;
  flex: 0 0 auto !important;
  gap: 16.19px !important;
  padding: 19.43px 32.39px !important;
}

.element .button-instance {
  color: var(--tertiary) !important;
  margin-top: -1.62px !important;
  white-space: unset !important;
}

</style>
