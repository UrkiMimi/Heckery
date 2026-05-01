#define MAX_DIST 10.0
#define MAX_LOOPS 20
#define EPSILON 0.01
#define PROJECTION_DIST 1.5

uniform sampler2D Noise

// https://www.shadertoy.com/view/ldl3Dl
vec3 voronoi( in vec3 x )
{
    vec3 p = floor( x );
    vec3 f = fract( x );

	float id = 0.0;
    vec2 res = vec2( 100.0 );
    for( int k=-1; k<=1; k++ )
    for( int j=-1; j<=1; j++ )
    for( int i=-1; i<=1; i++ )
    {
        vec3 b = vec3( float(i), float(j), float(k) );
        vec3 r = vec3( b ) - f;
        float d = dot( r, r );

        if( d < res.x )
        {
			id = dot( p+b, vec3(1.0,57.0,113.0 ) );
            res = vec2( d, res.x );			
        }
        else if( d < res.y )
        {
            res.y = d;
        }
    }

    return vec3( sqrt( res ), abs(id) );
}

vec3 rotateX(vec3 p, float a) {
   float c = cos(a);
   float s = sin(a);
   mat3 m = mat3(
       1, 0, 0,
       0, c, -s,
       0, s, c
   );
   return m * p;
}

vec3 rotateY(vec3 p, float a) {
   float c = cos(a);
   float s = sin(a);
   mat3 m = mat3(
       c, 0, s,
       0, 1, 0,
       -s, 0, c
   );
   return m * p;
}

vec3 rotateZ(vec3 p, float a) {
   float c = cos(a);
   float s = sin(a);
   mat3 m = mat3(
       c, -s, 0,
       s, c, 0,
       0, 0, 1
   );
   return m * p;
}

// https://iquilezles.org/articles/distfunctions2d/
float sdBox( vec3 p, vec3 b )
{
    vec3 q = abs(p) - b;
    return length(max(q,0.0)) + min(max(q.x,max(q.y,q.z)),0.0);
}

float map(vec3 p, float t) 
{
    vec3 boxPos = vec3(0, 0, 0.5);
    p -= boxPos;
    p = rotateX(p, pow(1.0 - t, 3.0) * sin(u_timer));
    p = rotateZ(p, u_timer * 0.6);
    return sdBox(p, vec3(0.5));
}

vec3 getNormal(vec3 p, float sceneDist, float t) 
{
    float xDistance = map(p + vec3(EPSILON, 0, 0), t);
    float yDistance = map(p + vec3(0, EPSILON, 0), t);
    float zDistance = map(p + vec3(0, 0, EPSILON), t);
    return (vec3(xDistance, yDistance, zDistance) - sceneDist) / EPSILON;
}

vec4 skybox(vec3 dir) 
{
    vec3 v = voronoi(dir * 2.0 + u_timer * 0.3);
    float vx = v.x;
    vec4 col = mix(vec4(-dir, 1), vec4(dir, 1), max(vx, 0.5));
    col += vec4(dir, 1) * v.y * v.y * 0.3;
    col = abs(col);
    return col;
}

vec3 viewToWorldDir(vec3 dir, float t) 
{
    float invT = 1.0 - t;
    float invT3 = invT * invT * invT;
    dir = rotateY(dir, invT * sin(u_timer * 0.5) * 3.0);
    return dir;
}

vec3 viewToWorldPos(vec3 p, float t) 
{
    p.z -= (1.0 - t) * 5.0;
    p = viewToWorldDir(p, t);
    return p;
}

vec4 marchReflection(vec3 p, vec3 dir, float t) {
    float d = 0.0;
    
    for (int i = 0; i < MAX_LOOPS && d < MAX_DIST; i++) 
    {
        float sceneDist = map(p, t);
        
        if (sceneDist < EPSILON) 
        {
            vec3 normal = getNormal(p, sceneDist, t);
            vec3 reflection = reflect(dir, normal);
            
            t -= 1.0;
            reflection.z *= -1.0;
            vec3 transformedRef = viewToWorldDir(reflection, 0.0);
            
            return skybox(transformedRef);
        }
        
        d += sceneDist;
        p += dir * sceneDist;
    }
    
    return skybox(dir);
}

vec4 march(vec3 p, vec3 dir, float t) 
{
    float d = 0.0;
    
    for (int i = 0; i < MAX_LOOPS && d < MAX_DIST; i++) 
    {
        float sceneDist = map(p, t);
        
        if (sceneDist < EPSILON) 
        {
            vec3 normal = getNormal(p, sceneDist, t);
            vec3 reflection = reflect(dir, normal);
            
            t -= 1.0;
            reflection.z *= -1.0;
            vec3 transformedRef = viewToWorldDir(reflection, 0.0);
            
            vec3 reflectionPos = viewToWorldPos(vec3(0), t);
            
            return marchReflection(reflectionPos, transformedRef, t);
        }
        
        d += sceneDist;
        p += dir * sceneDist;
    }
    
    return skybox(dir);
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    vec2 uv = fragCoord/iResolution.xy;
    float aspect = 480/360;
    
    vec2 camUV = uv * 2.0 - 1.0;
    camUV.x /= aspect;
    
    float t = mod(u_timer * 0.5, 1.0);
    vec3 camDir = normalize(vec3(camUV, PROJECTION_DIST));
    
    vec3 p = viewToWorldPos(vec3(0), t);
    vec3 dir = viewToWorldDir(camDir, t);
  
    fragColor = march(p, dir, t);
}