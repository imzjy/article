两点间插值函数
======

当我订阅在MouseMove事件的时候得到的点并不是等坐标距离的，也不是按像素的，为了让动画更加自然，需要用到两点间的线性插值。

```csharp
private List<Point> LinearInterpolated(List<Point> trackPoints)
{
    List<Point> result = new List<Point>();
    Point start = trackPoints[0];
    for (int i = 1; i < trackPoints.Count; i++)
    {
        Point end = trackPoints[i];
 
        var distance = Math.Floor(Math.Sqrt(Math.Pow((start.X - end.X), 2) + Math.Pow((start.Y - end.Y), 2)));
        //Debug.WriteLine("distance:" + distance.ToString());
 
        if (distance > 1)
        {
            var step = 1 / distance;
            var startRatio = 0.0;
            Point prePosition = start;
            for (int j = 0; j < distance; j++)
            {
                startRatio += step;
                Point r = Point.Empty;
 
                r.X = Convert.ToInt32(Math.Round(start.X + (end.X - start.X) * startRatio, 0));
                r.Y = Convert.ToInt32(Math.Round(start.Y + (end.Y - start.Y) * startRatio, 0));
 
                if (r != prePosition)
                {
                    result.Add(r);
                    prePosition = r;
                }
            }
        }
 
        start = end;
    }
 
    return result;
}
```
