
import ursina
from ursina import *
app = ursina.Ursina()
ray = Shader(
    name = 'raycast',
    vertex_code = '''
        #version 330
        uniform mat4 p3d_ModelViewProjectionMatrix;
        in vec4 p3d_Vertex;
        in vec2 p3d_MultiTexCoord0;
        out vec2 uv;
        void main() {
            gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
            uv = p3d_MultiTexCoord0;
        }
    ''',
    fragment_code = '''
        #version 330
        uniform sampler2D texture;
        in vec2 uv;
        out vec4 fragColor;
        void main() {
            vec4 color = texture2D(texture, uv);
            fragColor = vec4(color.rgb, 1.0);
        }
    ''',
    geometry_code = '''
        #version 330
        uniform mat4 p3d_ModelViewProjectionMatrix;
        layout(points) in;
        layout(triangle_strip, max_vertices = 4) out;
        in vec2 uv[];
        out vec2 g_uv;
        void main() {
            vec4 pos = gl_in[0].gl_Position;
            g_uv = uv[0];
            gl_Position = p3d_ModelViewProjectionMatrix * (pos + vec4(-1, -1, 0, 0));
            EmitVertex();
            g_uv = uv[0];
            gl_Position = p3d_ModelViewProjectionMatrix * (pos + vec4(1, -1, 0, 0));
            EmitVertex();
            g_uv = uv[0];
            gl_Position = p3d_ModelViewProjectionMatrix * (pos + vec4(-1, 1, 0, 0));
            EmitVertex();
            g_uv = uv[0];
            gl_Position = p3d_ModelViewProjectionMatrix * (pos + vec4(1, 1, 0, 0));
            EmitVertex();
            EndPrimitive();
        }
    '''
)
cube_1 = Entity(model = "cube", scale = 1,shader = ray, position = (0,20,0))
cube_1.set_shader_input('transform_matrix', cube_1.getNetTransform().getMat())
floor = Entity(model = "plane",scale = 100,shader = ray,position_z = -20)
EditorCamera()
app.run()
