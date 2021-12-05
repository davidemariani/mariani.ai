# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1638734524.8314102
_enable_loop = True
_template_filename = 'C:/Users/david/.conda/envs/mariani-ai/lib/site-packages/nikola/data/themes/base/templates/authors.tmpl'
_template_uri = 'authors.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        hidden_authors = _import_ns.get('hidden_authors', context.get('hidden_authors', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        items = _import_ns.get('items', context.get('items', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def extra_head():
            return render_extra_head(context)
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(kind=kind, feeds=False)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        hidden_authors = _import_ns.get('hidden_authors', context.get('hidden_authors', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        items = _import_ns.get('items', context.get('items', UNDEFINED))
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<article class="authorindex">\n')
        if items:
            __M_writer('        <h2>')
            __M_writer(str(messages("Authors")))
            __M_writer('</h2>\n        <div class="metadata">\n            ')
            __M_writer(str(feeds_translations.translation_link(kind)))
            __M_writer('\n        </div>\n        <ul class="postlist">\n')
            for text, link in items:
                if text not in hidden_authors:
                    __M_writer('                <li><a class="reference listtitle" href="')
                    __M_writer(str(link))
                    __M_writer('">')
                    __M_writer(filters.html_escape(str(text)))
                    __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/david/.conda/envs/mariani-ai/lib/site-packages/nikola/data/themes/base/templates/authors.tmpl", "uri": "authors.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "45": 2, "46": 3, "51": 7, "56": 25, "62": 5, "72": 5, "73": 6, "74": 6, "80": 9, "93": 9, "94": 11, "95": 12, "96": 12, "97": 12, "98": 14, "99": 14, "100": 17, "101": 18, "102": 19, "103": 19, "104": 19, "105": 19, "106": 19, "107": 22, "108": 24, "114": 108}}
__M_END_METADATA
"""
