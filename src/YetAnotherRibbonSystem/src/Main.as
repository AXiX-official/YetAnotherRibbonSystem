package
{
	import flash.display.Sprite;
    import flash.display.MovieClip;
    import flash.events.Event;
    import flash.display.Loader;
    import flash.net.URLRequest;
    import flash.utils.Timer;
	import lesta.api.ModBase;
    import flash.events.TimerEvent;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.utils.Dictionary;
	import flash.utils.setTimeout;
	
	/**
	 * ...
	 * @author AXiX_Official
	 */
	public class Main extends ModBase 
	{
        private var loader:Loader;
        private var animationQueue:Array = [];
        private var imageCache:Dictionary = new Dictionary();
        private var animationContainer:Sprite;
        public var levelImage:MovieClip;
        private var levelImageCache:Dictionary = new Dictionary();
		private var isShaking:Boolean = false;

        public function Main() {
            super();
        }
		
		override public function init():void 
		{
			super.init();
            gameAPI.data.call("mlog", ["Flash Init"]);
			gameAPI.data.addCallBack("Show", initAnimation);
            gameAPI.data.addCallBack("Clean", removeAllAnimation);
            gameAPI.data.addCallBack("Register", registerImage);
            gameAPI.data.addCallBack("RegisterLevel", registerLevelImage);
            gameAPI.data.addCallBack("HideAll", hideAllAnimations);
            gameAPI.data.addCallBack("ShowAll", showAllAnimations);
            gameAPI.data.addCallBack("UpdateLevel", updateLevel);
            gameAPI.data.addCallBack("ShakeLevel", shakeLevelImage);

            animationContainer = new Sprite();
            animationContainer.mouseEnabled = false;
            animationContainer.mouseChildren = false;
            gameAPI.stage.addChild(animationContainer);
		}

		override public function fini():void 
        {
            removeAllAnimation();
            
            gameAPI.data.removeCallBack();
            if (animationContainer)
            {
                gameAPI.stage.removeChild(animationContainer);
            }
            super.fini();
        }

        public function removeAllAnimation():void {
            // levelImage
            if (levelImage && animationContainer.contains(levelImage)) {
                animationContainer.removeChild(levelImage);
                levelImage = null;
            }
            while (animationQueue.length > 0) {
                var animation:MovieClip = animationQueue.pop();
                removeAnimation(animation);
            }
        }
		
		override public function updateStage(width:Number, height:Number):void 
		{
			super.updateStage(width, height);
		}

        private function registerImage(ribbon_id:int, file_path:String):void {
            var loader:Loader = new Loader();
            loader.contentLoaderInfo.addEventListener(Event.COMPLETE, function(event:Event):void {
                var bitmap:Bitmap = loader.content as Bitmap;
                if (bitmap && bitmap.bitmapData) {
                    imageCache[ribbon_id] = bitmap.bitmapData;
                    gameAPI.data.call("mlog", ["Image loaded for ribbon_id: " + ribbon_id]);
                } else {
                    gameAPI.data.call("mlog", ["Failed to load image for ribbon_id: " + ribbon_id]);
                }
            });
            loader.load(new URLRequest(file_path));
        }

        private function registerLevelImage(level:String, file_path:String):void {
            var loader:Loader = new Loader();
            loader.contentLoaderInfo.addEventListener(Event.COMPLETE, function(event:Event):void {
                var bitmap:Bitmap = loader.content as Bitmap;
                if (bitmap && bitmap.bitmapData) {
                    levelImageCache[level] = bitmap.bitmapData;
                } else {
                    gameAPI.data.call("mlog", ["Failed to load image for level: " + level]);
                }
            });
            loader.load(new URLRequest(file_path));
        }

        private function initAnimation(ribbon_id:int, existTime:int, alphaValue:Number = 0.7):void {
            if (!imageCache[ribbon_id]) {
                gameAPI.data.call("mlog", ["Image not found for ribbon_id: " + ribbon_id]);
                return;
            }

            var animation:MovieClip = new MovieClip();

            animation.addChild(new Bitmap(imageCache[ribbon_id].clone()));

            animation.alpha = alphaValue;

            animation.x = -animation.width;
            animation.y = animationQueue.length * animation.height;

            animationContainer.addChild(animation);

            animationQueue.push(animation);

            animation.addEventListener(Event.ENTER_FRAME, onEnterFrame);

            var timer:Timer = new Timer(existTime, 1);
            timer.addEventListener(TimerEvent.TIMER_COMPLETE, function(event:TimerEvent):void {
                removeAnimation(animation);
            });
            timer.start();
        }

        private function onEnterFrame(event:Event):void {
            var animation:MovieClip = event.currentTarget as MovieClip;
            if (animation.x < 0) {
                animation.x += 8;
            }

            var index:int = animationQueue.indexOf(animation);
            var targetY:Number = index * animation.height;
            if (animation.y > targetY) {
                animation.y -= (animation.y - targetY) * 0.1;
            }
            if (animation.y < targetY) {
                animation.y = targetY;
            }
        }

        private function removeAnimation(animation:MovieClip):void {
            animationContainer.removeChild(animation);
            animation.removeEventListener(Event.ENTER_FRAME, onEnterFrame);

            var index:int = animationQueue.indexOf(animation);
            if (index >= 0) {
                animationQueue.splice(index, 1);
            }
        }

        public function hideAllAnimations():void {
            gameAPI.stage.removeChild(animationContainer);
        }

        public function showAllAnimations():void {
            gameAPI.stage.addChild(animationContainer);
        }

        public function updateLevel(level:String, scaleFactor:Number = 1):void {
            if (levelImage) {
                animationContainer.removeChild(levelImage);
                levelImage = null;
            }
            var bitmapData:BitmapData = levelImageCache[level];
            if (bitmapData) {
                levelImage = new MovieClip();
                levelImage.mouseEnabled = false;
                levelImage.mouseChildren = false;

                var scaledBitmap:Bitmap = new Bitmap(bitmapData.clone());
                scaledBitmap.scaleX = scaleFactor;
                scaledBitmap.scaleY = scaleFactor;
                levelImage.addChild(scaledBitmap);

                levelImage.x = gameAPI.stage.width / 5 - levelImage.width / 2;
                levelImage.y = gameAPI.stage.height / 5 - levelImage.height / 2;

                animationContainer.addChild(levelImage);
            } else {
                gameAPI.data.call("mlog", ["Failed to load level image for level: " + level]);
            }
        }

        private function shakeLevelImage(shakeAmount:int, shakeDuration:int, shakeTimes:int):void {
			if (isShaking) {
				return;
			}
			
			isShaking = true;
			
            if (!levelImage) {
                gameAPI.data.call("mlog", ["No levelImage to shake"]);
                return;
            }

            var originalX:Number = levelImage.x;
            var originalY:Number = levelImage.y;

            for (var i:int = 0; i < shakeTimes; i++) {
                setTimeout(shakeImage, i * shakeDuration, originalX, originalY, shakeAmount);
                setTimeout(shakeImage, (i * shakeDuration) + (shakeDuration / 2), originalX, originalY, -shakeAmount);
            }

            setTimeout(function():void {
                levelImage.x = originalX;
                levelImage.y = originalY;
                isShaking = false;
            }, shakeTimes * shakeDuration);
        }

        private function shakeImage(originalX:Number, originalY:Number, shakeAmount:int):void {
            if (!levelImage) {
                return;
            }
            levelImage.x = originalX + (Math.random() * shakeAmount - shakeAmount / 2);
            levelImage.y = originalY + (Math.random() * shakeAmount - shakeAmount / 2);
        }
		
	}
	
}