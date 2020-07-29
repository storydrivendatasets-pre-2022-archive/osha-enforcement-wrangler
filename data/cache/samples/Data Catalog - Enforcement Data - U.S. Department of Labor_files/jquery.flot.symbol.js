/*
Flot plugin that adds some extra symbols for plotting points.

The symbols are accessed as strings through the standard symbol
choice:

  series: {
      points: {
          symbol: "square" // or "diamond", "triangle", "cross"
      }
  }

*/

(function ($) {
    function processRawData(plot, series, datapoints) {
        // we normalize the area of each symbol so it is approximately the
        // same as a circle of the given radius

        var handlers = {
            square: function (ctx, x, y, radius, shadow) {
				//x = x + radius*7/8;
				y = y - radius /2;
				radius = radius / 4;
                // pi * r^2 = (2s)^2  =>  s = r * sqrt(pi)/2
                //var size = radius * Math.sqrt(Math.PI) / 2;
                //ctx.rect(x - size, y - size, size + size, size + size);
				ctx.arc(x,y,radius,0,Math.PI*2,false);
				ctx.moveTo(x-radius*0.6,y+radius*1.1);
				ctx.lineTo(x+radius*0.6,y+radius*1.1);
				//ctx.moveTo(x-radius*0.6,y+radius*1.1);
				ctx.arc(x-radius*0.6,y+radius*2.1,radius,-Math.PI/2,Math.PI,true);
				ctx.lineTo(x-radius*1.6,y+radius*5);
				ctx.lineTo(x+radius*1.6,y+radius*5);
				ctx.arc(x+radius*0.6,y+radius*2.1,radius,0,-Math.PI/2,true);
				//ctx.lineTo(x+radius*1.6,y+radius*1.1);
				//ctx.lineTo(x-radius,y+radius*3);
            },
            diamond: function (ctx, x, y, radius, shadow) {
				//y= y-radius;
				//x=x-radius*7/8;
				ctx.lineCap="round";
				ctx.arc(x,y,radius,0,Math.PI*2,false);
				ctx.moveTo(x,y);
				ctx.lineTo(x,y-radius*0.6);
				ctx.moveTo(x,y);
				ctx.lineTo(x+radius*.5,y+radius*.35);
				//ctx.lineCap="butt";
                // pi * r^2 = 2s^2  =>  s = r * sqrt(pi/2)
				/*
                var size = radius * Math.sqrt(Math.PI / 2);
                ctx.moveTo(x - size, y);
                ctx.lineTo(x, y - size);
                ctx.lineTo(x + size, y);
                ctx.lineTo(x, y + size);
                ctx.lineTo(x - size, y);*/
            },
            triangle: function (ctx, x, y, radius, shadow) {
				//radius = radius;
                // pi * r^2 = 1/2 * s^2 * sin (pi / 3)  =>  s = r * sqrt(2 * pi / sin(pi / 3))
				ctx.moveTo(x-radius,y);
				ctx.lineTo(x+radius,y);
				ctx.lineTo(x+radius*6/8,y+radius);
				ctx.lineTo(x-radius*6/8,y+radius);
				ctx.lineTo(x-radius,y);
				ctx.moveTo(x-radius*4/8,y+radius);
				ctx.arc(x-radius*4/8,y+radius,radius*2/8,0,-Math.PI*2,true);
				ctx.moveTo(x+radius*4/8,y+radius);
				ctx.arc(x+radius*4/8,y+radius,radius*2/8,0,-Math.PI*2,true);
				ctx.moveTo(x-radius,y);
				ctx.arc(x+radius*5/8,y,radius*3/8,0,-Math.PI,true);
				ctx.arc(x-radius*5/8,y,radius*2/8,0,-Math.PI,true);
				ctx.arc(x-radius*0/8,y,radius*2/8,0,-Math.PI,true);
				ctx.moveTo(x-radius*4/8,y-radius*4/8);
				//ctx.arc(x,y,radius*5/8,-Math.PI*2/8,-Math.PI*6/8,true);
				//ctx.arc(x,y,radius*5/8,-Math.PI*2/8,-Math.PI*6/8,false);
				//ctx.arc(x-radius*4/8,y,radius*3/8,-Math.PI/2,-Math.PI,false);
				ctx.moveTo(x,y);
				//ctx.moveTo(x-radius,y);
				//ctx.arc(x+radius*6/8,y,radius*3/8,0,-Math.PI,true);
				/*
                var size = radius * Math.sqrt(2 * Math.PI / Math.sin(Math.PI / 3));
                var height = size * Math.sin(Math.PI / 3);
                ctx.moveTo(x - size/2, y + height/2);
                ctx.lineTo(x + size/2, y + height/2);
                if (!shadow) {
                    ctx.lineTo(x, y - height/2);
                    ctx.lineTo(x - size/2, y + height/2);
                }
				*/
            },
			
			symbol_Accident: function (ctx, x, y, radius, shadow) {
				//radius = radius;
                // pi * r^2 = 1/2 * s^2 * sin (pi / 3)  =>  s = r * sqrt(2 * pi / sin(pi / 3))
				ctx.moveTo(x-radius,y);
				ctx.lineTo(x+radius*4/8,y);
				ctx.lineTo(x+radius*6/8,y+radius*2);
				ctx.lineTo(x-radius*6/8,y+radius*2);
				ctx.lineTo(x-radius,y-radius);
				//ctx.moveTo(x-radius*4/8,y);
				//ctx.arc(x-radius*4/8,y+radius,radius*2/8,0,-Math.PI*2,true);
				//ctx.moveTo(x+radius*4/8,y+radius);
				//ctx.arc(x+radius*4/8,y+radius,radius*2/8,0,-Math.PI*2,true);
				//ctx.moveTo(x-radius,y);
				//ctx.arc(x+radius*5/8,y,radius*3/8,0,-Math.PI,true);
				//ctx.arc(x-radius*5/8,y,radius*2/8,0,-Math.PI,true);
				//ctx.arc(x-radius*0/8,y,radius*2/8,0,-Math.PI,true);
				//ctx.moveTo(x-radius*4/8,y-radius*4/8);
				//ctx.arc(x,y,radius*5/8,-Math.PI*2/8,-Math.PI*6/8,true);
				//ctx.arc(x,y,radius*5/8,-Math.PI*2/8,-Math.PI*6/8,false);
				//ctx.arc(x-radius*4/8,y,radius*3/8,-Math.PI/2,-Math.PI,false);
				//ctx.moveTo(x,y);
				//ctx.moveTo(x-radius,y);
				//ctx.arc(x+radius*6/8,y,radius*3/8,0,-Math.PI,true);
				/*
                var size = radius * Math.sqrt(2 * Math.PI / Math.sin(Math.PI / 3));
                var height = size * Math.sin(Math.PI / 3);
                ctx.moveTo(x - size/2, y + height/2);
                ctx.lineTo(x + size/2, y + height/2);
                if (!shadow) {
                    ctx.lineTo(x, y - height/2);
                    ctx.lineTo(x - size/2, y + height/2);
                }
				*/
            },
			
            cross: function (ctx, x, y, radius, shadow) {
                // pi * r^2 = (2s)^2  =>  s = r * sqrt(pi)/2
                var size = radius * Math.sqrt(Math.PI) / 2;
                ctx.moveTo(x - size, y - size);
                ctx.lineTo(x + size, y + size);
                ctx.moveTo(x - size, y + size);
                ctx.lineTo(x + size, y - size);
            }
        }

        var s = series.points.symbol;
        if (handlers[s])
            series.points.symbol = handlers[s];
    }
    
    function init(plot) {
        plot.hooks.processDatapoints.push(processRawData);
    }
    
    $.plot.plugins.push({
        init: init,
        name: 'symbols',
        version: '1.0'
    });
})(jQuery);
