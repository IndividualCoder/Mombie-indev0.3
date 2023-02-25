##import ursina
##from ursina import *
##
##
##
### create a 3d shader
##shsader = ursina.Shader(name = "test_shader",
##    vertex_code =
##    '''
##    #version 150
##    in vec3 in_position;
##    in vec3 in_normal;
##    out vec3 normal;
##    uniform mat4 matrix;
##
##    void main()
##    {
##        gl_Position = matrix * vec4(in_position, 1.0);
##        normal = in_normal;
##    }
##    ''',
##
##    fragment_code =
##    '''
##    #version 150
##    in vec3 normal;
##    out vec4 out_color;
##
##    void main()
##    {
##        out_color = vec4(normal, 1.0);
##    }
##    '''
##)
##
##
##if __name__ == '__main__':
##    from ursina import *
##    from ursina.prefabs.primitives import *
##    app = ursina.Ursina()
##    window.color=color.black
##
##    # e = Entity(model='sphere', shader=basic_lighting_shader)
##    # e.setShaderInput('transform_matrix', e.getNetTransform().getMat())
##    shader = shsader
##
##    a = WhiteCube(shader=shsader)
##    # a.setShaderInput('transform_matrix', a.getNetTransform().getMat())
##
##    b = WhiteSphere(shader=shsader, x=3)
##    # b.set_shader_input('transform_matrix', b.getNetTransform().getMat())
##    # AzureSphere(shader=a.shader, y=2)
##    GrayPlane(scale=10, y=-2, texture='shore', shader=shsader)
##
##    Sky(color=color.light_gray)
##    EditorCamera()
##
##    def update():
##        b.rotation_y += 1
##        #b.rotation_z += 1
##        b.rotation_x += 1
##        b.set_shader_input('transform_matrix', b.getNetTransform().getMat())
##    # EditorCamera()
##
##
##    # run the program
##    app.run()
##


##
##a = "Hello mr."
##print(a)
##b = input("What is your name")
##print("hello",b)

x = list('Sub')
y = sorted(x)
z = y
print(z)
























































